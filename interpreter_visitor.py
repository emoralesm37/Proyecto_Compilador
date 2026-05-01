# ================================================================
# interpreter_visitor.py  (v3)
# Visitor Intérprete — Ejecuta el AST validado
# Actualizado para gramatica_v3: arrays, break, continue, import
# ================================================================

from antlr4 import *
from gramatica_v3Parser  import gramatica_v3Parser
from gramatica_v3Visitor import gramatica_v3Visitor
from Tabla_de_simbolos   import TablaSimbolos


# ──────────────────────────────────────────────────────────────
# SEÑALES DE CONTROL DE FLUJO
# ──────────────────────────────────────────────────────────────

class ReturnSignal(Exception):
    """Propaga un valor de retorno desde una función."""
    def __init__(self, valor):
        self.valor = valor

class BreakSignal(Exception):
    """Sale del ciclo más interno (break)."""
    pass

class ContinueSignal(Exception):
    """Salta a la siguiente iteración del ciclo más interno (continue)."""
    pass


# ──────────────────────────────────────────────────────────────
# INTÉRPRETE
# ──────────────────────────────────────────────────────────────

class InterpreterVisitor(gramatica_v3Visitor):

    def __init__(self):
        self.tabla     = TablaSimbolos()
        self.funciones = {}   # nombre → FuncDeclContext

    # ──────────────────────────────────────────────────────────
    # PROGRAMA — dos pasadas
    # ──────────────────────────────────────────────────────────

    def visitProgram(self, ctx: gramatica_v3Parser.ProgramContext):
        nombre = ctx.ID().getText() if ctx.ID() else "programa"
        print("=" * 55)
        print(f"  Iniciando ejecución de '{nombre}'")
        print("=" * 55 + "\n")

        # Pasada 1: registrar funciones
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v3Parser.TopFuncDeclContext):
                nombre_f = decl.funcDecl().ID().getText()
                self.funciones[nombre_f] = decl.funcDecl()

        # Pasada 2: ejecutar sentencias en orden
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v3Parser.TopStatementContext):
                self.visit(decl.statement())

        print("\n" + "=" * 55)
        print("  Fin del programa")
        print("=" * 55)
        self.tabla.imprimir()

    # ──────────────────────────────────────────────────────────
    # IMPORT — simplemente se ignora en tiempo de ejecución
    # ──────────────────────────────────────────────────────────

    def visitTopImport(self, ctx: gramatica_v3Parser.TopImportContext):
        pass   # los imports no tienen efecto en el intérprete

    # ──────────────────────────────────────────────────────────
    # DECLARACIONES DE NIVEL SUPERIOR
    # ──────────────────────────────────────────────────────────

    def visitTopFuncDecl(self, ctx: gramatica_v3Parser.TopFuncDeclContext):
        pass   # ya registradas en la pasada 1

    def visitTopStatement(self, ctx: gramatica_v3Parser.TopStatementContext):
        self.visit(ctx.statement())

    # ──────────────────────────────────────────────────────────
    # SENTENCIAS
    # ──────────────────────────────────────────────────────────

    def visitVarDecl(self, ctx: gramatica_v3Parser.VarDeclContext):
        tipo   = ctx.t_type().getText()
        nombre = ctx.ID().getText()

        if ctx.expr():
            valor = self.convertir(self.visit(ctx.expr()), tipo)
        else:
            defaults = {'int': 0, 'float': 0.0, 'bool': False, 'string': ''}
            valor = defaults.get(tipo, None)

        self.tabla.declarar_variable(nombre, tipo, valor)
        print(f"  [Declaración] {tipo:8} {nombre:12} = {valor!r}")
        return valor

    def visitArrayDecl(self, ctx: gramatica_v3Parser.ArrayDeclContext):
        """Declara un arreglo: int[] nums = [1, 2, 3];"""
        # Determinar tipo base del arreglo
        texto_tipo = ctx.arrayType().getText()
        if 'int' in texto_tipo:
            tipo_base = 'int'
        elif 'float' in texto_tipo:
            tipo_base = 'float'
        elif 'bool' in texto_tipo:
            tipo_base = 'bool'
        else:
            tipo_base = 'string'

        nombre = ctx.ID().getText()

        if ctx.arrayLiteral():
            elementos = []
            for expr_ctx in ctx.arrayLiteral().expr():
                val = self.visit(expr_ctx)
                elementos.append(self.convertir(val, tipo_base))
            valor = elementos
        else:
            valor = []

        self.tabla.declarar_variable(nombre, f'{tipo_base}[]', valor)
        print(f"  [Array Decl]  {tipo_base}[] {nombre:12} = {valor!r}")
        return valor

    def visitAssignment(self, ctx: gramatica_v3Parser.AssignmentContext):
        nombre = ctx.ID().getText()
        tipo   = self.tabla.obtener_tipo(nombre)
        valor  = self.convertir(self.visit(ctx.expr()), tipo)
        self.tabla.asignar(nombre, valor)
        print(f"  [Asignación]  {nombre:12} = {valor!r}")
        return valor

    def visitArrayAssign(self, ctx: gramatica_v3Parser.ArrayAssignContext):
        """Asignación a elemento: nums[i] = valor;"""
        nombre = ctx.ID().getText()
        simbolo = self.tabla.buscar(nombre)
        if simbolo is None:
            raise Exception(f"[Error] Arreglo '{nombre}' no declarado.")

        arreglo = simbolo['valor']
        idx     = int(self.visit(ctx.expr(0)))
        tipo_base = simbolo['tipo'].replace('[]', '')
        valor   = self.convertir(self.visit(ctx.expr(1)), tipo_base)

        if not isinstance(arreglo, list):
            raise Exception(f"[Error] '{nombre}' no es un arreglo.")
        if idx < 0 or idx >= len(arreglo):
            raise Exception(
                f"[Error] Índice {idx} fuera de rango para '{nombre}' "
                f"(tamaño {len(arreglo)})."
            )

        arreglo[idx] = valor
        self.tabla.asignar(nombre, arreglo)
        print(f"  [Array Asign] {nombre}[{idx}] = {valor!r}")
        return valor

    def visitIfStatement(self, ctx: gramatica_v3Parser.IfStatementContext):
        condicion = bool(self.visit(ctx.expr()))
        print(f"  [IF]   condición → {condicion}")

        self.tabla.push_scope()
        if condicion:
            print("  [IF]   ejecutando rama TRUE")
            self.visit(ctx.block(0))
        elif ctx.ELSE():
            print("  [IF]   ejecutando rama ELSE")
            self.visit(ctx.block(1))
        self.tabla.pop_scope()

    def visitWhileStatement(self, ctx: gramatica_v3Parser.WhileStatementContext):
        iteracion = 0
        while bool(self.visit(ctx.expr())):
            iteracion += 1
            print(f"  [WHILE] iteración {iteracion}")
            self.tabla.push_scope()
            try:
                self.visit(ctx.block())
            except BreakSignal:
                self.tabla.pop_scope()
                print("  [WHILE] break — saliendo del ciclo")
                break
            except ContinueSignal:
                self.tabla.pop_scope()
                print("  [WHILE] continue — siguiente iteración")
                continue
            self.tabla.pop_scope()

    def visitForStatement(self, ctx: gramatica_v3Parser.ForStatementContext):
        self.tabla.push_scope()
        self.visit(ctx.forInit())
        iteracion = 0
        while bool(self.visit(ctx.expr())):
            iteracion += 1
            print(f"  [FOR] iteración {iteracion}")
            try:
                self.visit(ctx.block())
            except BreakSignal:
                print("  [FOR] break — saliendo del ciclo")
                break
            except ContinueSignal:
                print("  [FOR] continue — siguiente iteración")
            self.visit(ctx.forUpdate())
        self.tabla.pop_scope()

    def visitForInitDecl(self, ctx: gramatica_v3Parser.ForInitDeclContext):
        tipo   = ctx.t_type().getText()
        nombre = ctx.ID().getText()
        valor  = self.convertir(self.visit(ctx.expr()), tipo)
        self.tabla.declarar_variable(nombre, tipo, valor)

    def visitForInitAssign(self, ctx: gramatica_v3Parser.ForInitAssignContext):
        nombre = ctx.ID().getText()
        tipo   = self.tabla.obtener_tipo(nombre)
        valor  = self.convertir(self.visit(ctx.expr()), tipo)
        self.tabla.asignar(nombre, valor)

    def visitForUpdate(self, ctx: gramatica_v3Parser.ForUpdateContext):
        nombre = ctx.ID().getText()
        tipo   = self.tabla.obtener_tipo(nombre)
        valor  = self.convertir(self.visit(ctx.expr()), tipo)
        self.tabla.asignar(nombre, valor)

    def visitReturnStatement(self, ctx: gramatica_v3Parser.ReturnStatementContext):
        valor = self.visit(ctx.expr()) if ctx.expr() else None
        raise ReturnSignal(valor)

    def visitBreakStatement(self, ctx: gramatica_v3Parser.BreakStatementContext):
        raise BreakSignal()

    def visitContinueStatement(self, ctx: gramatica_v3Parser.ContinueStatementContext):
        raise ContinueSignal()

    def visitPrintStatement(self, ctx: gramatica_v3Parser.PrintStatementContext):
        valor = self.visit(ctx.expr())
        print(valor)
        return valor

    def visitExprStatement(self, ctx: gramatica_v3Parser.ExprStatementContext):
        return self.visit(ctx.expr())

    def visitBlock(self, ctx: gramatica_v3Parser.BlockContext):
        return self.visitChildren(ctx)

    # ──────────────────────────────────────────────────────────
    # LLAMADA A FUNCIÓN
    # ──────────────────────────────────────────────────────────

    def visitFuncCallExpr(self, ctx: gramatica_v3Parser.FuncCallExprContext):
        nombre = ctx.ID().getText()

        if nombre not in self.funciones:
            raise Exception(f"[Error] Función '{nombre}' no encontrada.")

        func_ctx = self.funciones[nombre]

        # Evaluar argumentos ANTES de entrar al nuevo scope
        args_vals = []
        if ctx.argList():
            for arg in ctx.argList().expr():
                args_vals.append(self.visit(arg))

        # Obtener parámetros
        params = []
        if func_ctx.paramList():
            for p in func_ctx.paramList().param():
                params.append((p.t_type().getText(), p.ID().getText()))

        # Crear nuevo scope
        self.tabla.push_scope()

        # Ligar parámetros
        for (tipo_p, nombre_p), val in zip(params, args_vals):
            self.tabla.declarar_variable(nombre_p, tipo_p,
                                         self.convertir(val, tipo_p))

        # Ejecutar cuerpo
        resultado = None
        try:
            self.visit(func_ctx.block())
        except ReturnSignal as r:
            resultado = r.valor

        self.tabla.pop_scope()
        return resultado

    # ──────────────────────────────────────────────────────────
    # EXPRESIONES ARITMÉTICAS Y LÓGICAS
    # ──────────────────────────────────────────────────────────

    def visitMulExpr(self, ctx: gramatica_v3Parser.MulExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()

        if op == '*':
            return izq * der
        elif op == '/':
            if der == 0:
                raise Exception("[Error] División por cero.")
            return izq / der if isinstance(izq, float) or isinstance(der, float) \
                else izq // der
        elif op == '%':
            if der == 0:
                raise Exception("[Error] Módulo por cero.")
            return izq % der

    def visitAddExpr(self, ctx: gramatica_v3Parser.AddExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()
        return izq + der if op == '+' else izq - der

    def visitRelExpr(self, ctx: gramatica_v3Parser.RelExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()
        ops = {
            '==': lambda a, b: a == b,
            '!=': lambda a, b: a != b,
            '<>': lambda a, b: a != b,
            '<' : lambda a, b: a <  b,
            '>' : lambda a, b: a >  b,
            '<=': lambda a, b: a <= b,
            '>=': lambda a, b: a >= b,
        }
        return ops[op](izq, der)

    def visitAndExpr(self, ctx: gramatica_v3Parser.AndExprContext):
        return bool(self.visit(ctx.expr(0))) and bool(self.visit(ctx.expr(1)))

    def visitOrExpr(self, ctx: gramatica_v3Parser.OrExprContext):
        return bool(self.visit(ctx.expr(0))) or bool(self.visit(ctx.expr(1)))

    def visitNotExpr(self, ctx: gramatica_v3Parser.NotExprContext):
        return not bool(self.visit(ctx.expr()))

    def visitNegExpr(self, ctx: gramatica_v3Parser.NegExprContext):
        return -self.visit(ctx.expr())

    def visitParenExpr(self, ctx: gramatica_v3Parser.ParenExprContext):
        return self.visit(ctx.expr())

    # ──────────────────────────────────────────────────────────
    # ACCESO A ARREGLOS
    # ──────────────────────────────────────────────────────────

    def visitArrayAccessExpr(self, ctx: gramatica_v3Parser.ArrayAccessExprContext):
        """Acceso por índice: nums[i]"""
        nombre  = ctx.ID().getText()
        simbolo = self.tabla.buscar(nombre)

        if simbolo is None:
            raise Exception(f"[Error] Arreglo '{nombre}' no declarado.")

        arreglo = simbolo['valor']
        idx     = int(self.visit(ctx.expr()))

        if not isinstance(arreglo, list):
            raise Exception(f"[Error] '{nombre}' no es un arreglo.")
        if idx < 0 or idx >= len(arreglo):
            raise Exception(
                f"[Error] Índice {idx} fuera de rango para '{nombre}' "
                f"(tamaño {len(arreglo)})."
            )

        return arreglo[idx]

    # ──────────────────────────────────────────────────────────
    # LITERALES
    # ──────────────────────────────────────────────────────────

    def visitNumExpr(self, ctx: gramatica_v3Parser.NumExprContext):
        return int(ctx.NUM().getText())

    def visitFloatExpr(self, ctx: gramatica_v3Parser.FloatExprContext):
        return float(ctx.FLOAT_LIT().getText())

    def visitBoolExpr(self, ctx: gramatica_v3Parser.BoolExprContext):
        return ctx.BOOL_LIT().getText() == 'true'

    def visitStringExpr(self, ctx: gramatica_v3Parser.StringExprContext):
        return ctx.STRING_LIT().getText()[1:-1]   # quitar comillas

    def visitIdExpr(self, ctx: gramatica_v3Parser.IdExprContext):
        nombre  = ctx.ID().getText()
        simbolo = self.tabla.buscar(nombre)
        if simbolo is None:
            raise Exception(f"[Error] Variable '{nombre}' no fue declarada.")
        return simbolo['valor']

    # ──────────────────────────────────────────────────────────
    # CONVERSIÓN DE TIPOS
    # ──────────────────────────────────────────────────────────

    def convertir(self, valor, tipo: str):
        # Para tipos de arreglo no se convierte el contenido aquí
        if tipo.endswith('[]'):
            return valor if isinstance(valor, list) else []
        if tipo == 'int':    return int(valor)   if valor is not None else 0
        if tipo == 'float':  return float(valor) if valor is not None else 0.0
        if tipo == 'bool':   return bool(valor)
        if tipo == 'string': return str(valor)   if valor is not None else ''
        return valor
