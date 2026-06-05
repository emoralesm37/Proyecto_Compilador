# ================================================================
# ir_generator_v4.py
# Visitor Generador de LLVM IR usando llvmlite — v4
# Novedades: switch/case, operador ternario, cast explícito, structs
# Produce un módulo .ll verificable con: llvm-as archivo.ll
# Ejecutable con:                         lli archivo.ll
# ================================================================

from antlr4 import *
from gramatica_v4Parser  import gramatica_v4Parser
from gramatica_v4Visitor import gramatica_v4Visitor

from llvmlite import ir


# ──────────────────────────────────────────────────────────────
# MAPEO DE TIPOS ESCALARES
# ──────────────────────────────────────────────────────────────
TIPO_LLVM = {
    'int':    ir.IntType(32),
    'float':  ir.DoubleType(),
    'bool':   ir.IntType(1),
    'string': ir.IntType(8).as_pointer(),
}

DEFAULTS_LLVM = {
    'int':   ir.Constant(ir.IntType(32),  0),
    'float': ir.Constant(ir.DoubleType(), 0.0),
    'bool':  ir.Constant(ir.IntType(1),   0),
}

MAX_ARRAY = 256


class IRGenerator(gramatica_v4Visitor):

    def __init__(self):
        self.modulo   = ir.Module(name="programa_v4")
        self.modulo.triple = "x86_64-pc-linux-gnu"
        self.builder: ir.IRBuilder = None

        # variables: nombre → (alloca, tipo_str)
        self.variables: dict[str, tuple] = {}
        # funciones declaradas: nombre → ir.Function
        self.funciones: dict[str, ir.Function] = {}

        # Structs LLVM: nombre_struct → ir.LiteralStructType
        self._struct_llvm_types: dict[str, ir.LiteralStructType] = {}
        # Campos de structs: nombre_struct → {campo: (índice, tipo_str)}
        self._struct_fields: dict[str, dict[str, tuple[int, str]]] = {}

        # Pila para break/continue (ciclos)
        self._pila_ciclos: list[tuple] = []
        # Pila para break en switch
        self._pila_switch_break: list[ir.Block] = []

        # Contador para nombres únicos de globales
        self._str_counter = 0

        self._setup_printf()

    # ──────────────────────────────────────────────────────────
    # CONFIGURACIÓN INICIAL
    # ──────────────────────────────────────────────────────────

    def _setup_printf(self):
        voidptr_ty  = ir.IntType(8).as_pointer()
        printf_type = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self._printf_func = ir.Function(self.modulo, printf_type, name="printf")

    def _global_str(self, texto: str) -> ir.GlobalVariable:
        self._str_counter += 1
        encoded  = (texto + '\0').encode('utf-8')
        arr_type = ir.ArrayType(ir.IntType(8), len(encoded))
        gvar     = ir.GlobalVariable(self.modulo, arr_type,
                                     name=f".str{self._str_counter}")
        gvar.global_constant = True
        gvar.linkage         = 'internal'
        gvar.initializer     = ir.Constant(arr_type, bytearray(encoded))
        return gvar

    def _get_tipo_llvm(self, tipo_str: str) -> ir.Type:
        if tipo_str in TIPO_LLVM:
            return TIPO_LLVM[tipo_str]
        # Tipo struct
        if tipo_str in self._struct_llvm_types:
            return self._struct_llvm_types[tipo_str]
        return ir.IntType(32)   # fallback

    def _alloca(self, nombre: str, tipo_llvm: ir.Type) -> ir.AllocaInstr:
        with self.builder.goto_entry_block():
            return self.builder.alloca(tipo_llvm, name=nombre)

    def obtener_ir(self) -> str:
        return str(self.modulo)

    def guardar(self, ruta: str):
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(str(self.modulo))

    # ──────────────────────────────────────────────────────────
    # PROGRAMA
    # ──────────────────────────────────────────────────────────

    def visitProgram(self, ctx: gramatica_v4Parser.ProgramContext):
        # Pasada 1: registrar structs (antes que funciones)
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v4Parser.TopStructDeclContext):
                self._registrar_struct(decl.structDecl())

        # Pasada 2: registrar firmas de funciones
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v4Parser.TopFuncDeclContext):
                self._registrar_firma(decl.funcDecl())

        # Crear función main
        main_type  = ir.FunctionType(ir.IntType(32), [])
        main_func  = ir.Function(self.modulo, main_type, name="main")
        entry_blk  = main_func.append_basic_block("entry")
        self.builder = ir.IRBuilder(entry_blk)

        # Pasada 3: generar cuerpos de funciones
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v4Parser.TopFuncDeclContext):
                self.visit(decl)

        # Reactivar main para las sentencias del programa
        self.builder = ir.IRBuilder(entry_blk)

        # Pasada 4: sentencias principales
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v4Parser.TopStatementContext):
                self.visit(decl.statement())

        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(ir.IntType(32), 0))

    # ──────────────────────────────────────────────────────────
    # STRUCTS (novedad v4)
    # ──────────────────────────────────────────────────────────

    def _registrar_struct(self, ctx: gramatica_v4Parser.StructDeclContext):
        """Crea el tipo LLVM LiteralStructType y registra los campos."""
        nombre  = ctx.ID().getText()
        campos  = {}
        tipos_llvm = []

        for i, campo in enumerate(ctx.structField()):
            tipo_c   = campo.t_type().getText()
            nombre_c = campo.ID().getText()
            campos[nombre_c] = (i, tipo_c)
            tipos_llvm.append(self._get_tipo_llvm(tipo_c))

        struct_tipo = ir.LiteralStructType(tipos_llvm)
        self._struct_llvm_types[nombre] = struct_tipo
        self._struct_fields[nombre]     = campos

    def visitTopStructDecl(self, ctx: gramatica_v4Parser.TopStructDeclContext):
        pass   # ya registrado en la pasada 1

    def visitStructVarDecl(self, ctx: gramatica_v4Parser.StructVarDeclContext):
        """Punto p;  →  alloca del tipo struct"""
        tipo_struct = ctx.ID(0).getText()
        nombre_var  = ctx.ID(1).getText()

        if tipo_struct not in self._struct_llvm_types:
            raise Exception(f"[IR] Struct '{tipo_struct}' no fue declarado.")

        struct_tipo = self._struct_llvm_types[tipo_struct]
        alloca      = self._alloca(nombre_var, struct_tipo)
        self.variables[nombre_var] = (alloca, tipo_struct)

    def visitFieldAssign(self, ctx: gramatica_v4Parser.FieldAssignContext):
        """p.x = expr  →  GEP + store al campo x del struct"""
        nombre_var   = ctx.ID(0).getText()
        nombre_campo = ctx.ID(1).getText()
        alloca, tipo_struct = self.variables[nombre_var]

        idx_campo, tipo_campo_str = self._struct_fields[tipo_struct][nombre_campo]
        tipo_campo_llvm = self._get_tipo_llvm(tipo_campo_str)

        valor = self.visit(ctx.expr())
        valor = self._coerce(valor, tipo_campo_llvm)

        ptr = self.builder.gep(
            alloca,
            [ir.Constant(ir.IntType(32), 0),
             ir.Constant(ir.IntType(32), idx_campo)],
            inbounds=True
        )
        self.builder.store(valor, ptr)

    # ──────────────────────────────────────────────────────────
    # FUNCIONES
    # ──────────────────────────────────────────────────────────

    def _registrar_firma(self, ctx: gramatica_v4Parser.FuncDeclContext):
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

    def visitTopFuncDecl(self, ctx: gramatica_v4Parser.TopFuncDeclContext):
        self.visit(ctx.funcDecl())

    def visitFuncDecl(self, ctx: gramatica_v4Parser.FuncDeclContext):
        nombre = ctx.ID().getText()
        func   = self.funciones[nombre]

        entry_blk        = func.append_basic_block("entry")
        builder_previo   = self.builder
        variables_previas = self.variables.copy()

        self.builder   = ir.IRBuilder(entry_blk)
        self.variables = {}

        if ctx.paramList():
            for param_ctx, arg in zip(ctx.paramList().param(), func.args):
                nombre_p  = param_ctx.ID().getText()
                tipo_p    = param_ctx.t_type().getText()
                tipo_llvm = self._get_tipo_llvm(tipo_p)
                alloca    = self._alloca(nombre_p, tipo_llvm)
                self.builder.store(arg, alloca)
                self.variables[nombre_p] = (alloca, tipo_p)

        self.visit(ctx.block())

        if not self.builder.block.is_terminated:
            tipo_retorno = ctx.returnType().getText()
            if tipo_retorno == 'void':
                self.builder.ret_void()
            else:
                self.builder.ret(DEFAULTS_LLVM.get(tipo_retorno,
                                  ir.Constant(ir.IntType(32), 0)))

        self.builder   = builder_previo
        self.variables = variables_previas

    # ──────────────────────────────────────────────────────────
    # SENTENCIAS
    # ──────────────────────────────────────────────────────────

    def visitVarDecl(self, ctx: gramatica_v4Parser.VarDeclContext):
        tipo      = ctx.t_type().getText()
        nombre    = ctx.ID().getText()
        tipo_llvm = self._get_tipo_llvm(tipo)
        alloca    = self._alloca(nombre, tipo_llvm)
        self.variables[nombre] = (alloca, tipo)

        valor = self.visit(ctx.expr()) if ctx.expr() \
                else DEFAULTS_LLVM.get(tipo, ir.Constant(tipo_llvm, 0))
        valor = self._coerce(valor, tipo_llvm)
        self.builder.store(valor, alloca)

    def visitArrayDecl(self, ctx: gramatica_v4Parser.ArrayDeclContext):
        texto = ctx.arrayType().getText()
        if 'int' in texto:    tipo_base = 'int'
        elif 'float' in texto: tipo_base = 'float'
        elif 'bool' in texto:  tipo_base = 'bool'
        else:                  tipo_base = 'string'

        nombre    = ctx.ID().getText()
        tipo_llvm = self._get_tipo_llvm(tipo_base)
        size      = len(ctx.arrayLiteral().expr()) if ctx.arrayLiteral() else MAX_ARRAY
        arr_tipo  = ir.ArrayType(tipo_llvm, max(size, 1))
        alloca    = self._alloca(nombre, arr_tipo)
        self.variables[nombre] = (alloca, f'{tipo_base}[]')

        if ctx.arrayLiteral():
            for i, expr_ctx in enumerate(ctx.arrayLiteral().expr()):
                val = self._coerce(self.visit(expr_ctx), tipo_llvm)
                ptr = self.builder.gep(
                    alloca,
                    [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), i)],
                    inbounds=True
                )
                self.builder.store(val, ptr)

    def visitAssignment(self, ctx: gramatica_v4Parser.AssignmentContext):
        nombre = ctx.ID().getText()
        alloca, tipo = self.variables[nombre]
        valor = self._coerce(self.visit(ctx.expr()), self._get_tipo_llvm(tipo))
        self.builder.store(valor, alloca)

    def visitArrayAssign(self, ctx: gramatica_v4Parser.ArrayAssignContext):
        nombre = ctx.ID().getText()
        alloca, tipo = self.variables[nombre]
        tipo_base = tipo.replace('[]', '')
        tipo_llvm = self._get_tipo_llvm(tipo_base)
        idx   = self.visit(ctx.expr(0))
        valor = self._coerce(self.visit(ctx.expr(1)), tipo_llvm)
        ptr   = self.builder.gep(alloca,
                                  [ir.Constant(ir.IntType(32), 0), idx],
                                  inbounds=True)
        self.builder.store(valor, ptr)

    def visitIfStatement(self, ctx: gramatica_v4Parser.IfStatementContext):
        cond = self._to_bool(self.visit(ctx.expr()))
        func = self.builder.function

        blk_true  = func.append_basic_block("if_true")
        blk_false = func.append_basic_block("if_false")
        blk_fin   = func.append_basic_block("if_end")

        self.builder.cbranch(cond, blk_true, blk_false)

        self.builder = ir.IRBuilder(blk_true)
        self.visit(ctx.block(0))
        if not self.builder.block.is_terminated:
            self.builder.branch(blk_fin)

        self.builder = ir.IRBuilder(blk_false)
        if ctx.ELSE():
            self.visit(ctx.block(1))
        if not self.builder.block.is_terminated:
            self.builder.branch(blk_fin)

        self.builder = ir.IRBuilder(blk_fin)

    def visitWhileStatement(self, ctx: gramatica_v4Parser.WhileStatementContext):
        func       = self.builder.function
        blk_cond   = func.append_basic_block("while_cond")
        blk_cuerpo = func.append_basic_block("while_body")
        blk_fin    = func.append_basic_block("while_end")

        self._pila_ciclos.append((blk_cond, blk_fin))
        self.builder.branch(blk_cond)

        self.builder = ir.IRBuilder(blk_cond)
        cond = self._to_bool(self.visit(ctx.expr()))
        self.builder.cbranch(cond, blk_cuerpo, blk_fin)

        self.builder = ir.IRBuilder(blk_cuerpo)
        self.visit(ctx.block())
        if not self.builder.block.is_terminated:
            self.builder.branch(blk_cond)

        self.builder = ir.IRBuilder(blk_fin)
        self._pila_ciclos.pop()

    def visitForStatement(self, ctx: gramatica_v4Parser.ForStatementContext):
        func       = self.builder.function
        blk_cond   = func.append_basic_block("for_cond")
        blk_cuerpo = func.append_basic_block("for_body")
        blk_update = func.append_basic_block("for_update")
        blk_fin    = func.append_basic_block("for_end")

        self._pila_ciclos.append((blk_update, blk_fin))
        self.visit(ctx.forInit())
        self.builder.branch(blk_cond)

        self.builder = ir.IRBuilder(blk_cond)
        cond = self._to_bool(self.visit(ctx.expr()))
        self.builder.cbranch(cond, blk_cuerpo, blk_fin)

        self.builder = ir.IRBuilder(blk_cuerpo)
        self.visit(ctx.block())
        if not self.builder.block.is_terminated:
            self.builder.branch(blk_update)

        self.builder = ir.IRBuilder(blk_update)
        self.visit(ctx.forUpdate())
        if not self.builder.block.is_terminated:
            self.builder.branch(blk_cond)

        self.builder = ir.IRBuilder(blk_fin)
        self._pila_ciclos.pop()

    def visitSwitchStatement(self, ctx: gramatica_v4Parser.SwitchStatementContext):
        """
        Genera una instrucción switch nativa de LLVM.
        Requiere que los valores de los cases sean constantes enteras.
        """
        func      = self.builder.function
        blk_fin   = func.append_basic_block("switch_end")
        blk_def   = func.append_basic_block("switch_default")

        self._pila_switch_break.append(blk_fin)

        # Valor de control (debe ser entero)
        ctrl_val = self.visit(ctx.expr())
        if not isinstance(ctrl_val.type, ir.IntType):
            ctrl_val = self.builder.fptosi(ctrl_val, ir.IntType(32))

        # Crear instrucción switch
        sw = self.builder.switch(ctrl_val, blk_def)

        # Generar bloque para cada case
        bloques_case = []
        for case_clause in ctx.caseClause():
            blk = func.append_basic_block("switch_case")
            bloques_case.append(blk)

            # El valor del case debe ser un literal entero constante
            val_raw = self.visit(case_clause.expr())
            if isinstance(val_raw, ir.Constant):
                val_int = self._coerce(val_raw, ir.IntType(32))
            else:
                # Fallback: intentar convertir
                val_int = ir.Constant(ir.IntType(32), 0)

            sw.add_case(val_int, blk)

        # Generar cuerpo de cada case
        for i, (case_clause, blk_case) in enumerate(
                zip(ctx.caseClause(), bloques_case)):
            self.builder = ir.IRBuilder(blk_case)
            for stmt in case_clause.statement():
                self.visit(stmt)
            # Fall-through al siguiente case si no hay break/return
            if not self.builder.block.is_terminated:
                siguiente = (bloques_case[i + 1]
                             if i + 1 < len(bloques_case) else blk_def)
                self.builder.branch(siguiente)

        # Bloque default
        self.builder = ir.IRBuilder(blk_def)
        if ctx.defaultClause():
            for stmt in ctx.defaultClause().statement():
                self.visit(stmt)
        if not self.builder.block.is_terminated:
            self.builder.branch(blk_fin)

        self.builder = ir.IRBuilder(blk_fin)
        self._pila_switch_break.pop()

    def visitForInitDecl(self, ctx: gramatica_v4Parser.ForInitDeclContext):
        tipo   = ctx.t_type().getText()
        nombre = ctx.ID().getText()
        tipo_llvm = self._get_tipo_llvm(tipo)
        alloca = self._alloca(nombre, tipo_llvm)
        self.variables[nombre] = (alloca, tipo)
        valor  = self._coerce(self.visit(ctx.expr()), tipo_llvm)
        self.builder.store(valor, alloca)

    def visitForInitAssign(self, ctx: gramatica_v4Parser.ForInitAssignContext):
        nombre = ctx.ID().getText()
        alloca, tipo = self.variables[nombre]
        valor  = self._coerce(self.visit(ctx.expr()), self._get_tipo_llvm(tipo))
        self.builder.store(valor, alloca)

    def visitForUpdate(self, ctx: gramatica_v4Parser.ForUpdateContext):
        nombre = ctx.ID().getText()
        alloca, tipo = self.variables[nombre]
        valor  = self._coerce(self.visit(ctx.expr()), self._get_tipo_llvm(tipo))
        self.builder.store(valor, alloca)

    def visitReturnStatement(self, ctx: gramatica_v4Parser.ReturnStatementContext):
        if ctx.expr():
            self.builder.ret(self.visit(ctx.expr()))
        else:
            self.builder.ret_void()

    def visitBreakStatement(self, ctx: gramatica_v4Parser.BreakStatementContext):
        # Prioridad: switch > ciclo
        if self._pila_switch_break:
            self.builder.branch(self._pila_switch_break[-1])
        elif self._pila_ciclos:
            self.builder.branch(self._pila_ciclos[-1][1])

        func     = self.builder.function
        blk_dead = func.append_basic_block("after_break")
        self.builder = ir.IRBuilder(blk_dead)

    def visitContinueStatement(self, ctx: gramatica_v4Parser.ContinueStatementContext):
        if self._pila_ciclos:
            self.builder.branch(self._pila_ciclos[-1][0])
        func     = self.builder.function
        blk_dead = func.append_basic_block("after_continue")
        self.builder = ir.IRBuilder(blk_dead)

    def visitPrintStatement(self, ctx: gramatica_v4Parser.PrintStatementContext):
        valor = self.visit(ctx.expr())
        self._emitir_print(valor)

    def visitExprStatement(self, ctx: gramatica_v4Parser.ExprStatementContext):
        self.visit(ctx.expr())

    def visitBlock(self, ctx: gramatica_v4Parser.BlockContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    # ──────────────────────────────────────────────────────────
    # EXPRESIONES NUEVAS v4
    # ──────────────────────────────────────────────────────────

    def visitTernaryExpr(self, ctx: gramatica_v4Parser.TernaryExprContext):
        """
        cond ? expr_v : expr_f
        Genera bloques condicionales + phi node para unificar el resultado.
        """
        func      = self.builder.function
        blk_true  = func.append_basic_block("ternary_true")
        blk_false = func.append_basic_block("ternary_false")
        blk_merge = func.append_basic_block("ternary_merge")

        cond = self._to_bool(self.visit(ctx.expr(0)))
        self.builder.cbranch(cond, blk_true, blk_false)

        # Rama verdadera
        self.builder = ir.IRBuilder(blk_true)
        val_verd = self.visit(ctx.expr(1))
        blk_true_end = self.builder.block
        if not self.builder.block.is_terminated:
            self.builder.branch(blk_merge)

        # Rama falsa
        self.builder = ir.IRBuilder(blk_false)
        val_falso = self.visit(ctx.expr(2))
        blk_false_end = self.builder.block
        if not self.builder.block.is_terminated:
            self.builder.branch(blk_merge)

        # Merge con phi node
        self.builder = ir.IRBuilder(blk_merge)
        tipo_result  = val_verd.type

        # Unificar tipos si es necesario
        if val_verd.type != val_falso.type:
            if isinstance(val_verd.type, ir.DoubleType):
                tipo_result = ir.DoubleType()
            else:
                tipo_result = val_verd.type

        phi = self.builder.phi(tipo_result, name="ternary_result")
        phi.add_incoming(self._coerce(val_verd,  tipo_result), blk_true_end)
        phi.add_incoming(self._coerce(val_falso, tipo_result), blk_false_end)
        return phi

    def visitCastExpr(self, ctx: gramatica_v4Parser.CastExprContext):
        """
        (float) miVar  →  instrucciones de conversión de tipos LLVM
        """
        tipo_dest_str = ctx.t_type().getText()
        tipo_dest_llvm = self._get_tipo_llvm(tipo_dest_str)
        valor = self.visit(ctx.expr())
        return self._coerce(valor, tipo_dest_llvm)

    def visitFieldAccessExpr(self, ctx: gramatica_v4Parser.FieldAccessExprContext):
        """p.x  →  GEP al campo x + load"""
        nombre_var   = ctx.ID(0).getText()
        nombre_campo = ctx.ID(1).getText()
        alloca, tipo_struct = self.variables[nombre_var]

        idx_campo, tipo_campo_str = self._struct_fields[tipo_struct][nombre_campo]
        ptr = self.builder.gep(
            alloca,
            [ir.Constant(ir.IntType(32), 0),
             ir.Constant(ir.IntType(32), idx_campo)],
            inbounds=True
        )
        return self.builder.load(ptr)

    # ──────────────────────────────────────────────────────────
    # EXPRESIONES (heredadas de v3)
    # ──────────────────────────────────────────────────────────

    def visitMulExpr(self, ctx: gramatica_v4Parser.MulExprContext):
        izq, der = self._unificar_tipos(self.visit(ctx.expr(0)),
                                         self.visit(ctx.expr(1)))
        op = ctx.getChild(1).getText()
        if isinstance(izq.type, ir.DoubleType):
            if op == '*': return self.builder.fmul(izq, der)
            if op == '/': return self.builder.fdiv(izq, der)
            if op == '%': return self.builder.frem(izq, der)
        else:
            if op == '*': return self.builder.mul(izq, der)
            if op == '/': return self.builder.sdiv(izq, der)
            if op == '%': return self.builder.srem(izq, der)

    def visitAddExpr(self, ctx: gramatica_v4Parser.AddExprContext):
        izq, der = self._unificar_tipos(self.visit(ctx.expr(0)),
                                         self.visit(ctx.expr(1)))
        op = ctx.getChild(1).getText()
        if isinstance(izq.type, ir.DoubleType):
            return self.builder.fadd(izq, der) if op == '+' \
                   else self.builder.fsub(izq, der)
        return self.builder.add(izq, der) if op == '+' \
               else self.builder.sub(izq, der)

    def visitRelExpr(self, ctx: gramatica_v4Parser.RelExprContext):
        izq, der = self._unificar_tipos(self.visit(ctx.expr(0)),
                                         self.visit(ctx.expr(1)))
        op = ctx.getChild(1).getText()
        mapa = {'==': '==', '!=': '!=', '<>': '!=',
                '<': '<',  '>': '>',  '<=': '<=', '>=': '>='}
        if isinstance(izq.type, ir.DoubleType):
            return self.builder.fcmp_ordered(mapa[op], izq, der)
        return self.builder.icmp_signed(mapa[op], izq, der)

    def visitAndExpr(self, ctx: gramatica_v4Parser.AndExprContext):
        return self.builder.and_(self.visit(ctx.expr(0)),
                                  self.visit(ctx.expr(1)))

    def visitOrExpr(self, ctx: gramatica_v4Parser.OrExprContext):
        return self.builder.or_(self.visit(ctx.expr(0)),
                                 self.visit(ctx.expr(1)))

    def visitNotExpr(self, ctx: gramatica_v4Parser.NotExprContext):
        return self.builder.not_(self.visit(ctx.expr()))

    def visitNegExpr(self, ctx: gramatica_v4Parser.NegExprContext):
        op = self.visit(ctx.expr())
        return self.builder.fneg(op) if isinstance(op.type, ir.DoubleType) \
               else self.builder.neg(op)

    def visitArrayAccessExpr(self, ctx: gramatica_v4Parser.ArrayAccessExprContext):
        nombre = ctx.ID().getText()
        alloca, _ = self.variables[nombre]
        idx = self.visit(ctx.expr())
        ptr = self.builder.gep(alloca,
                               [ir.Constant(ir.IntType(32), 0), idx],
                               inbounds=True)
        return self.builder.load(ptr)

    def visitFuncCallExpr(self, ctx: gramatica_v4Parser.FuncCallExprContext):
        nombre = ctx.ID().getText()
        func   = self.funciones[nombre]
        args   = []
        if ctx.argList():
            for i, arg_ctx in enumerate(ctx.argList().expr()):
                val = self._coerce(self.visit(arg_ctx), func.args[i].type)
                args.append(val)
        return self.builder.call(func, args)

    def visitParenExpr(self, ctx: gramatica_v4Parser.ParenExprContext):
        return self.visit(ctx.expr())

    # ── Literales ──
    def visitNumExpr(self, ctx):
        return ir.Constant(ir.IntType(32), int(ctx.NUM().getText()))

    def visitFloatExpr(self, ctx):
        return ir.Constant(ir.DoubleType(), float(ctx.FLOAT_LIT().getText()))

    def visitBoolExpr(self, ctx):
        val = 1 if ctx.BOOL_LIT().getText() == 'true' else 0
        return ir.Constant(ir.IntType(1), val)

    def visitStringExpr(self, ctx):
        texto = ctx.STRING_LIT().getText()[1:-1]
        gvar  = self._global_str(texto)
        return self.builder.gep(
            gvar,
            [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), 0)],
            inbounds=True
        )

    def visitIdExpr(self, ctx):
        nombre = ctx.ID().getText()
        alloca, _ = self.variables[nombre]
        return self.builder.load(alloca)

    # ──────────────────────────────────────────────────────────
    # HELPERS DE TIPOS
    # ──────────────────────────────────────────────────────────

    def _coerce(self, valor: ir.Value, tipo_dest: ir.Type) -> ir.Value:
        """Convierte entre tipos escalares cuando sea necesario."""
        if valor.type == tipo_dest:
            return valor
        # int → double
        if isinstance(tipo_dest, ir.DoubleType) and isinstance(valor.type, ir.IntType):
            return self.builder.sitofp(valor, tipo_dest)
        # double → int
        if isinstance(tipo_dest, ir.IntType) and isinstance(valor.type, ir.DoubleType):
            return self.builder.fptosi(valor, tipo_dest)
        # bool (i1) → int (i32)
        if isinstance(tipo_dest, ir.IntType) and valor.type == ir.IntType(1):
            return self.builder.zext(valor, tipo_dest)
        # int (i32) → bool (i1)
        if tipo_dest == ir.IntType(1) and isinstance(valor.type, ir.IntType):
            return self.builder.icmp_signed(
                '!=', valor, ir.Constant(valor.type, 0)
            )
        return valor

    def _unificar_tipos(self, izq: ir.Value, der: ir.Value):
        if isinstance(izq.type, ir.DoubleType) and isinstance(der.type, ir.IntType):
            der = self.builder.sitofp(der, ir.DoubleType())
        elif isinstance(der.type, ir.DoubleType) and isinstance(izq.type, ir.IntType):
            izq = self.builder.sitofp(izq, ir.DoubleType())
        return izq, der

    def _to_bool(self, valor: ir.Value) -> ir.Value:
        """Convierte cualquier valor a i1 para usar en condiciones."""
        if valor.type == ir.IntType(1):
            return valor
        if isinstance(valor.type, ir.DoubleType):
            return self.builder.fcmp_ordered(
                '!=', valor, ir.Constant(ir.DoubleType(), 0.0)
            )
        return self.builder.icmp_signed(
            '!=', valor, ir.Constant(valor.type, 0)
        )

    def _emitir_print(self, valor: ir.Value):
        self._str_counter += 1
        tipo = valor.type

        if tipo == ir.IntType(32):
            fmt = "%d\n"
        elif tipo == ir.DoubleType():
            fmt = "%f\n"
        elif tipo == ir.IntType(1):
            fmt = "%d\n"
            valor = self.builder.zext(valor, ir.IntType(32))
        else:
            fmt = "%s\n"

        gvar = self._global_str(fmt)
        ptr  = self.builder.gep(
            gvar,
            [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), 0)],
            inbounds=True
        )
        self.builder.call(self._printf_func, [ptr, valor])
