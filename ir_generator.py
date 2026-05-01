# ================================================================
# ir_generator.py
# Visitor Generador de LLVM IR usando llvmlite
# Produce un módulo .ll compilable con: llvm-as archivo.ll
# Ejecutable con:                        lli archivo.ll
# ================================================================

from antlr4 import *
from gramatica_v3Parser  import gramatica_v3Parser
from gramatica_v3Visitor import gramatica_v3Visitor

from llvmlite import ir
import llvmlite.binding as llvm


# ──────────────────────────────────────────────────────────────
# MAPEO DE TIPOS: lenguaje → LLVM IR
# ──────────────────────────────────────────────────────────────
TIPO_LLVM = {
    'int':    ir.IntType(32),
    'float':  ir.DoubleType(),
    'bool':   ir.IntType(1),
    'string': ir.IntType(8).as_pointer(),   # char*
}

DEFAULTS_LLVM = {
    'int':   ir.Constant(ir.IntType(32),   0),
    'float': ir.Constant(ir.DoubleType(),  0.0),
    'bool':  ir.Constant(ir.IntType(1),    0),
}

MAX_ARRAY = 256   # tamaño máximo para arreglos estáticos


class IRGenerator(gramatica_v3Visitor):

    def __init__(self):
        # Módulo LLVM raíz
        self.modulo   = ir.Module(name="programa")
        self.modulo.triple = "x86_64-pc-linux-gnu"

        # Builder activo (se actualiza al entrar/salir de funciones)
        self.builder: ir.IRBuilder = None

        # Tabla de variables: nombre → alloca (ir.AllocaInstr)
        self.variables: dict = {}

        # Tabla de funciones declaradas: nombre → ir.Function
        self.funciones: dict = {}

        # Pila de bloques de break/continue
        # cada entrada = (bloque_continue, bloque_break)
        self._pila_ciclos: list = []

        # Configurar printf una sola vez
        self._printf_func = None
        self._setup_printf()

    # ──────────────────────────────────────────────────────────
    # UTILIDADES
    # ──────────────────────────────────────────────────────────

    def _setup_printf(self):
        """Declara printf como función externa en el módulo."""
        voidptr_ty  = ir.IntType(8).as_pointer()
        printf_type = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self._printf_func = ir.Function(self.modulo, printf_type, name="printf")

    def _global_str(self, texto: str, nombre: str = ".str") -> ir.GlobalVariable:
        """Crea una cadena global constante para printf."""
        encoded = (texto + '\0').encode('utf-8')
        tipo_str = ir.ArrayType(ir.IntType(8), len(encoded))
        gvar = ir.GlobalVariable(self.modulo, tipo_str, name=nombre)
        gvar.global_constant = True
        gvar.linkage = 'internal'
        gvar.initializer = ir.Constant(tipo_str, bytearray(encoded))
        return gvar

    def _get_tipo_llvm(self, tipo_str: str) -> ir.Type:
        return TIPO_LLVM.get(tipo_str, ir.IntType(32))

    def _map_tipo(self, ctx_tipo) -> str:
        """Extrae el nombre de tipo (string) desde el contexto ANTLR."""
        return ctx_tipo.getText()

    def _alloca(self, nombre: str, tipo_llvm: ir.Type) -> ir.AllocaInstr:
        """Crea una instrucción alloca al inicio del bloque entry de la función."""
        with self.builder.goto_entry_block():
            return self.builder.alloca(tipo_llvm, name=nombre)

    def obtener_ir(self) -> str:
        """Retorna el módulo LLVM IR como string."""
        return str(self.modulo)

    def guardar(self, ruta: str):
        """Escribe el módulo en un archivo .ll"""
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(str(self.modulo))

    # ──────────────────────────────────────────────────────────
    # PROGRAMA
    # ──────────────────────────────────────────────────────────

    def visitProgram(self, ctx: gramatica_v3Parser.ProgramContext):
        # Pasada 1: registrar firmas de todas las funciones
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v3Parser.TopFuncDeclContext):
                self._registrar_firma(decl.funcDecl())

        # Crear función main
        main_type = ir.FunctionType(ir.IntType(32), [])
        main_func = ir.Function(self.modulo, main_type, name="main")
        entry_block = main_func.append_basic_block("entry")
        self.builder = ir.IRBuilder(entry_block)

        # Pasada 2: generar funciones de usuario
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v3Parser.TopFuncDeclContext):
                self.visit(decl)

        # Reactivar builder de main para el código principal
        self.builder = ir.IRBuilder(entry_block)

        # Pasada 3: generar sentencias principales
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v3Parser.TopStatementContext):
                self.visit(decl.statement())

        # Retornar 0 desde main
        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(ir.IntType(32), 0))

    def _registrar_firma(self, ctx: gramatica_v3Parser.FuncDeclContext):
        """Registra la firma de una función sin generar su cuerpo."""
        nombre       = ctx.ID().getText()
        tipo_retorno = ctx.returnType().getText()
        tipo_ret_llvm = (ir.VoidType() if tipo_retorno == 'void'
                         else self._get_tipo_llvm(tipo_retorno))

        tipos_param = []
        if ctx.paramList():
            for p in ctx.paramList().param():
                tipos_param.append(self._get_tipo_llvm(p.t_type().getText()))

        func_type = ir.FunctionType(tipo_ret_llvm, tipos_param)
        func      = ir.Function(self.modulo, func_type, name=nombre)
        self.funciones[nombre] = func

    # ──────────────────────────────────────────────────────────
    # FUNCIONES
    # ──────────────────────────────────────────────────────────

    def visitTopFuncDecl(self, ctx: gramatica_v3Parser.TopFuncDeclContext):
        self.visit(ctx.funcDecl())

    def visitFuncDecl(self, ctx: gramatica_v3Parser.FuncDeclContext):
        nombre = ctx.ID().getText()
        func   = self.funciones[nombre]

        # Crear bloque entry de la función
        entry_block = func.append_basic_block("entry")
        # Guardar builder anterior
        builder_previo   = self.builder
        variables_previas = self.variables.copy()

        self.builder   = ir.IRBuilder(entry_block)
        self.variables = {}

        # Ligar parámetros a allocas
        if ctx.paramList():
            for param_ctx, arg in zip(ctx.paramList().param(), func.args):
                nombre_p  = param_ctx.ID().getText()
                tipo_p    = param_ctx.t_type().getText()
                tipo_llvm = self._get_tipo_llvm(tipo_p)
                alloca    = self._alloca(nombre_p, tipo_llvm)
                self.builder.store(arg, alloca)
                self.variables[nombre_p] = (alloca, tipo_p)

        # Generar cuerpo
        self.visit(ctx.block())

        # Bloque de retorno implícito void
        if not self.builder.block.is_terminated:
            tipo_retorno = ctx.returnType().getText()
            if tipo_retorno == 'void':
                self.builder.ret_void()
            else:
                self.builder.ret(DEFAULTS_LLVM.get(tipo_retorno,
                                  ir.Constant(ir.IntType(32), 0)))

        # Restaurar contexto
        self.builder   = builder_previo
        self.variables = variables_previas

    # ──────────────────────────────────────────────────────────
    # SENTENCIAS
    # ──────────────────────────────────────────────────────────

    def visitVarDecl(self, ctx: gramatica_v3Parser.VarDeclContext):
        tipo   = ctx.t_type().getText()
        nombre = ctx.ID().getText()
        tipo_llvm = self._get_tipo_llvm(tipo)

        alloca = self._alloca(nombre, tipo_llvm)
        self.variables[nombre] = (alloca, tipo)

        if ctx.expr():
            valor = self.visit(ctx.expr())
            valor = self._coerce(valor, tipo_llvm)
        else:
            valor = DEFAULTS_LLVM.get(tipo, ir.Constant(tipo_llvm, 0))

        self.builder.store(valor, alloca)

    def visitArrayDecl(self, ctx: gramatica_v3Parser.ArrayDeclContext):
        """Declara un arreglo como alloca de array estático."""
        # Determinar el tipo base del array
        texto = ctx.arrayType().getText()
        if 'int' in texto:
            tipo_base = 'int'
        elif 'float' in texto:
            tipo_base = 'float'
        elif 'bool' in texto:
            tipo_base = 'bool'
        else:
            tipo_base = 'string'

        nombre    = ctx.ID().getText()
        tipo_llvm = self._get_tipo_llvm(tipo_base)

        # Contar elementos para el tamaño del array
        size = MAX_ARRAY
        if ctx.arrayLiteral():
            size = max(len(ctx.arrayLiteral().expr()), 1)

        arr_tipo = ir.ArrayType(tipo_llvm, size)
        alloca   = self._alloca(nombre, arr_tipo)
        self.variables[nombre] = (alloca, f'{tipo_base}[]')

        # Inicializar elementos
        if ctx.arrayLiteral():
            for i, expr_ctx in enumerate(ctx.arrayLiteral().expr()):
                valor = self.visit(expr_ctx)
                valor = self._coerce(valor, tipo_llvm)
                ptr   = self.builder.gep(alloca,
                                         [ir.Constant(ir.IntType(32), 0),
                                          ir.Constant(ir.IntType(32), i)],
                                         inbounds=True)
                self.builder.store(valor, ptr)

    def visitAssignment(self, ctx: gramatica_v3Parser.AssignmentContext):
        nombre = ctx.ID().getText()
        alloca, tipo = self.variables[nombre]
        tipo_llvm = self._get_tipo_llvm(tipo)
        valor = self.visit(ctx.expr())
        valor = self._coerce(valor, tipo_llvm)
        self.builder.store(valor, alloca)

    def visitArrayAssign(self, ctx: gramatica_v3Parser.ArrayAssignContext):
        nombre = ctx.ID().getText()
        alloca, tipo = self.variables[nombre]
        tipo_base = tipo.replace('[]', '')
        tipo_llvm = self._get_tipo_llvm(tipo_base)

        idx   = self.visit(ctx.expr(0))
        valor = self.visit(ctx.expr(1))
        valor = self._coerce(valor, tipo_llvm)

        ptr = self.builder.gep(alloca,
                               [ir.Constant(ir.IntType(32), 0), idx],
                               inbounds=True)
        self.builder.store(valor, ptr)

    def visitIfStatement(self, ctx: gramatica_v3Parser.IfStatementContext):
        cond = self.visit(ctx.expr())
        # Asegurar que sea i1
        if cond.type != ir.IntType(1):
            cond = self.builder.icmp_signed('!=', cond,
                                            ir.Constant(cond.type, 0))

        func = self.builder.function
        blk_true  = func.append_basic_block("if_true")
        blk_false = func.append_basic_block("if_false")
        blk_fin   = func.append_basic_block("if_end")

        self.builder.cbranch(cond, blk_true, blk_false)

        # Rama verdadera
        self.builder = ir.IRBuilder(blk_true)
        self.visit(ctx.block(0))
        if not self.builder.block.is_terminated:
            self.builder.branch(blk_fin)

        # Rama falsa
        self.builder = ir.IRBuilder(blk_false)
        if ctx.ELSE():
            self.visit(ctx.block(1))
        if not self.builder.block.is_terminated:
            self.builder.branch(blk_fin)

        self.builder = ir.IRBuilder(blk_fin)

    def visitWhileStatement(self, ctx: gramatica_v3Parser.WhileStatementContext):
        func = self.builder.function
        blk_cond   = func.append_basic_block("while_cond")
        blk_cuerpo = func.append_basic_block("while_body")
        blk_fin    = func.append_basic_block("while_end")

        self._push_loop(blk_cond, blk_fin)
        self.builder.branch(blk_cond)

        # Bloque condición
        self.builder = ir.IRBuilder(blk_cond)
        cond = self.visit(ctx.expr())
        if cond.type != ir.IntType(1):
            cond = self.builder.icmp_signed('!=', cond,
                                            ir.Constant(cond.type, 0))
        self.builder.cbranch(cond, blk_cuerpo, blk_fin)

        # Bloque cuerpo
        self.builder = ir.IRBuilder(blk_cuerpo)
        self.visit(ctx.block())
        if not self.builder.block.is_terminated:
            self.builder.branch(blk_cond)

        self.builder = ir.IRBuilder(blk_fin)
        self._pop_loop()

    def visitForStatement(self, ctx: gramatica_v3Parser.ForStatementContext):
        func = self.builder.function
        blk_cond   = func.append_basic_block("for_cond")
        blk_cuerpo = func.append_basic_block("for_body")
        blk_update = func.append_basic_block("for_update")
        blk_fin    = func.append_basic_block("for_end")

        self._push_loop(blk_update, blk_fin)

        # Init
        self.visit(ctx.forInit())
        self.builder.branch(blk_cond)

        # Condición
        self.builder = ir.IRBuilder(blk_cond)
        cond = self.visit(ctx.expr())
        if cond.type != ir.IntType(1):
            cond = self.builder.icmp_signed('!=', cond,
                                            ir.Constant(cond.type, 0))
        self.builder.cbranch(cond, blk_cuerpo, blk_fin)

        # Cuerpo
        self.builder = ir.IRBuilder(blk_cuerpo)
        self.visit(ctx.block())
        if not self.builder.block.is_terminated:
            self.builder.branch(blk_update)

        # Update
        self.builder = ir.IRBuilder(blk_update)
        self.visit(ctx.forUpdate())
        if not self.builder.block.is_terminated:
            self.builder.branch(blk_cond)

        self.builder = ir.IRBuilder(blk_fin)
        self._pop_loop()

    def visitForInitDecl(self, ctx: gramatica_v3Parser.ForInitDeclContext):
        tipo   = ctx.t_type().getText()
        nombre = ctx.ID().getText()
        tipo_llvm = self._get_tipo_llvm(tipo)
        alloca = self._alloca(nombre, tipo_llvm)
        self.variables[nombre] = (alloca, tipo)
        valor = self.visit(ctx.expr())
        valor = self._coerce(valor, tipo_llvm)
        self.builder.store(valor, alloca)

    def visitForInitAssign(self, ctx: gramatica_v3Parser.ForInitAssignContext):
        nombre = ctx.ID().getText()
        alloca, tipo = self.variables[nombre]
        tipo_llvm = self._get_tipo_llvm(tipo)
        valor = self.visit(ctx.expr())
        valor = self._coerce(valor, tipo_llvm)
        self.builder.store(valor, alloca)

    def visitForUpdate(self, ctx: gramatica_v3Parser.ForUpdateContext):
        nombre = ctx.ID().getText()
        alloca, tipo = self.variables[nombre]
        tipo_llvm = self._get_tipo_llvm(tipo)
        valor = self.visit(ctx.expr())
        valor = self._coerce(valor, tipo_llvm)
        self.builder.store(valor, alloca)

    def visitReturnStatement(self, ctx: gramatica_v3Parser.ReturnStatementContext):
        if ctx.expr():
            valor = self.visit(ctx.expr())
            self.builder.ret(valor)
        else:
            self.builder.ret_void()

    def visitBreakStatement(self, ctx: gramatica_v3Parser.BreakStatementContext):
        blk_fin = self._loop_fin_actual()
        self.builder.branch(blk_fin)
        # Crear bloque muerto para instrucciones después del break
        func = self.builder.function
        blk_dead = func.append_basic_block("after_break")
        self.builder = ir.IRBuilder(blk_dead)

    def visitContinueStatement(self, ctx: gramatica_v3Parser.ContinueStatementContext):
        blk_continue = self._loop_inicio_actual()
        self.builder.branch(blk_continue)
        func = self.builder.function
        blk_dead = func.append_basic_block("after_continue")
        self.builder = ir.IRBuilder(blk_dead)

    def visitPrintStatement(self, ctx: gramatica_v3Parser.PrintStatementContext):
        """Emite una llamada a printf para imprimir el resultado."""
        valor = self.visit(ctx.expr())
        self._emitir_print(valor)

    def visitExprStatement(self, ctx: gramatica_v3Parser.ExprStatementContext):
        self.visit(ctx.expr())

    def visitBlock(self, ctx: gramatica_v3Parser.BlockContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    # ──────────────────────────────────────────────────────────
    # PRINT helper
    # ──────────────────────────────────────────────────────────

    _str_counter = 0

    def _emitir_print(self, valor: ir.Value):
        """Selecciona el formato correcto y llama a printf."""
        self._str_counter += 1
        tipo = valor.type

        if tipo == ir.IntType(32):
            fmt_str = "%d\n"
        elif tipo == ir.DoubleType():
            fmt_str = "%f\n"
        elif tipo == ir.IntType(1):
            # bool: imprimir 0/1
            fmt_str = "%d\n"
            valor   = self.builder.zext(valor, ir.IntType(32))
        else:
            # string (i8*)
            fmt_str = "%s\n"

        gvar = self._global_str(fmt_str, f".fmt{self._str_counter}")
        ptr  = self.builder.gep(gvar,
                                [ir.Constant(ir.IntType(32), 0),
                                 ir.Constant(ir.IntType(32), 0)],
                                inbounds=True)
        self.builder.call(self._printf_func, [ptr, valor])

    # ──────────────────────────────────────────────────────────
    # EXPRESIONES
    # ──────────────────────────────────────────────────────────

    def visitMulExpr(self, ctx: gramatica_v3Parser.MulExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()
        izq, der = self._unificar_tipos(izq, der)

        if isinstance(izq.type, ir.DoubleType):
            if op == '*':  return self.builder.fmul(izq, der)
            if op == '/':  return self.builder.fdiv(izq, der)
            if op == '%':  return self.builder.frem(izq, der)
        else:
            if op == '*':  return self.builder.mul(izq, der)
            if op == '/':  return self.builder.sdiv(izq, der)
            if op == '%':  return self.builder.srem(izq, der)

    def visitAddExpr(self, ctx: gramatica_v3Parser.AddExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()
        izq, der = self._unificar_tipos(izq, der)

        if isinstance(izq.type, ir.DoubleType):
            return self.builder.fadd(izq, der) if op == '+' \
                   else self.builder.fsub(izq, der)
        else:
            return self.builder.add(izq, der) if op == '+' \
                   else self.builder.sub(izq, der)

    def visitRelExpr(self, ctx: gramatica_v3Parser.RelExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()
        izq, der = self._unificar_tipos(izq, der)

        ops_int  = {'==': '==', '!=': '!=', '<>': '!=',
                    '<': '<',  '>': '>',  '<=': '<=', '>=': '>='}
        ops_real = {'==': '==', '!=': '!=', '<>': '!=',
                    '<': '<',  '>': '>',  '<=': '<=', '>=': '>='}

        if isinstance(izq.type, ir.DoubleType):
            return self.builder.fcmp_ordered(ops_real[op], izq, der)
        else:
            return self.builder.icmp_signed(ops_int[op], izq, der)

    def visitAndExpr(self, ctx: gramatica_v3Parser.AndExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        return self.builder.and_(izq, der)

    def visitOrExpr(self, ctx: gramatica_v3Parser.OrExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        return self.builder.or_(izq, der)

    def visitNotExpr(self, ctx: gramatica_v3Parser.NotExprContext):
        operando = self.visit(ctx.expr())
        return self.builder.not_(operando)

    def visitNegExpr(self, ctx: gramatica_v3Parser.NegExprContext):
        operando = self.visit(ctx.expr())
        if isinstance(operando.type, ir.DoubleType):
            return self.builder.fneg(operando)
        return self.builder.neg(operando)

    def visitArrayAccessExpr(self, ctx: gramatica_v3Parser.ArrayAccessExprContext):
        nombre = ctx.ID().getText()
        alloca, tipo = self.variables[nombre]
        idx = self.visit(ctx.expr())
        ptr = self.builder.gep(alloca,
                               [ir.Constant(ir.IntType(32), 0), idx],
                               inbounds=True)
        return self.builder.load(ptr)

    def visitFuncCallExpr(self, ctx: gramatica_v3Parser.FuncCallExprContext):
        nombre = ctx.ID().getText()
        func   = self.funciones[nombre]
        args   = []
        if ctx.argList():
            for i, arg_ctx in enumerate(ctx.argList().expr()):
                val = self.visit(arg_ctx)
                tipo_param = func.args[i].type
                val = self._coerce(val, tipo_param)
                args.append(val)
        return self.builder.call(func, args)

    def visitParenExpr(self, ctx: gramatica_v3Parser.ParenExprContext):
        return self.visit(ctx.expr())

    # ──────────────────────────────────────────────────────────
    # LITERALES
    # ──────────────────────────────────────────────────────────

    def visitNumExpr(self, ctx: gramatica_v3Parser.NumExprContext):
        return ir.Constant(ir.IntType(32), int(ctx.NUM().getText()))

    def visitFloatExpr(self, ctx: gramatica_v3Parser.FloatExprContext):
        return ir.Constant(ir.DoubleType(), float(ctx.FLOAT_LIT().getText()))

    def visitBoolExpr(self, ctx: gramatica_v3Parser.BoolExprContext):
        val = 1 if ctx.BOOL_LIT().getText() == 'true' else 0
        return ir.Constant(ir.IntType(1), val)

    def visitStringExpr(self, ctx: gramatica_v3Parser.StringExprContext):
        texto = ctx.STRING_LIT().getText()[1:-1]   # quitar comillas
        self._str_counter += 1
        gvar = self._global_str(texto, f".str{self._str_counter}")
        return self.builder.gep(gvar,
                                [ir.Constant(ir.IntType(32), 0),
                                 ir.Constant(ir.IntType(32), 0)],
                                inbounds=True)

    def visitIdExpr(self, ctx: gramatica_v3Parser.IdExprContext):
        nombre = ctx.ID().getText()
        alloca, _ = self.variables[nombre]
        return self.builder.load(alloca)

    # ──────────────────────────────────────────────────────────
    # HELPERS DE TIPOS
    # ──────────────────────────────────────────────────────────

    def _coerce(self, valor: ir.Value, tipo_destino: ir.Type) -> ir.Value:
        """Convierte int→double o double→int si es necesario."""
        if valor.type == tipo_destino:
            return valor
        if isinstance(tipo_destino, ir.DoubleType) and isinstance(valor.type, ir.IntType):
            return self.builder.sitofp(valor, tipo_destino)
        if isinstance(tipo_destino, ir.IntType) and isinstance(valor.type, ir.DoubleType):
            return self.builder.fptosi(valor, tipo_destino)
        return valor

    def _unificar_tipos(self, izq: ir.Value, der: ir.Value):
        """Si uno es double y otro int, convierte el int a double."""
        if isinstance(izq.type, ir.DoubleType) and isinstance(der.type, ir.IntType):
            der = self.builder.sitofp(der, ir.DoubleType())
        elif isinstance(der.type, ir.DoubleType) and isinstance(izq.type, ir.IntType):
            izq = self.builder.sitofp(izq, ir.DoubleType())
        return izq, der

    # ──────────────────────────────────────────────────────────
    # SOPORTE BREAK / CONTINUE
    # ──────────────────────────────────────────────────────────

    def _push_loop(self, blk_continue: ir.Block, blk_break: ir.Block):
        self._pila_ciclos.append((blk_continue, blk_break))

    def _pop_loop(self):
        if self._pila_ciclos:
            self._pila_ciclos.pop()

    def _loop_inicio_actual(self) -> ir.Block:
        return self._pila_ciclos[-1][0]

    def _loop_fin_actual(self) -> ir.Block:
        return self._pila_ciclos[-1][1]
