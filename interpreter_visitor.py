# ================================================================
# interpreter_visitor.py
# Visitor Intérprete — Ejecuta el AST y procesa print
# Solo se ejecuta si el análisis semántico pasó sin errores
# ================================================================

from antlr4 import *
from ExpresionesParser  import ExpresionesParser
from ExpresionesVisitor import ExpresionesVisitor
from Tabla_de_simbolos  import TablaSimbolos


class ReturnSignal(Exception):
    """Señal para propagar un valor de retorno de función."""
    def __init__(self, valor):
        self.valor = valor


class InterpreterVisitor(ExpresionesVisitor):

    def __init__(self):
        self.tabla     = TablaSimbolos()
        self.funciones = {}   # nombre → FuncDeclContext

    # ──────────────────────────────────────────────────────────
    # PROGRAMA — dos pasadas
    # ──────────────────────────────────────────────────────────

    def visitProgram(self, ctx: ExpresionesParser.ProgramContext):
        print("=" * 55)
        print("  Iniciando ejecución del programa")
        print("=" * 55 + "\n")

        # Pasada 1: registrar funciones
        for decl in ctx.topLevelDecl():
            if isinstance(decl, ExpresionesParser.TopFuncDeclContext):
                nombre = decl.funcDecl().ID().getText()
                self.funciones[nombre] = decl.funcDecl()

        # Pasada 2: ejecutar sentencias en orden
        for decl in ctx.topLevelDecl():
            if isinstance(decl, ExpresionesParser.TopStatementContext):
                self.visit(decl.statement())

        print("\n" + "=" * 55)
        print("  Fin del programa")
        print("=" * 55)
        self.tabla.imprimir()

    # ──────────────────────────────────────────────────────────
    # SENTENCIAS
    # ──────────────────────────────────────────────────────────

    def visitVarDecl(self, ctx: ExpresionesParser.VarDeclContext):
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

    def visitAssignment(self, ctx: ExpresionesParser.AssignmentContext):
        nombre = ctx.ID().getText()
        tipo   = self.tabla.obtener_tipo(nombre)
        valor  = self.convertir(self.visit(ctx.expr()), tipo)
        self.tabla.asignar(nombre, valor)
        print(f"  [Asignación]  {nombre:12} = {valor!r}")
        return valor

    def visitIfStatement(self, ctx: ExpresionesParser.IfStatementContext):
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

    def visitWhileStatement(self, ctx: ExpresionesParser.WhileStatementContext):
        iteracion = 0
        while bool(self.visit(ctx.expr())):
            iteracion += 1
            print(f"  [WHILE] iteración {iteracion}")
            self.tabla.push_scope()
            self.visit(ctx.block())
            self.tabla.pop_scope()

    def visitForStatement(self, ctx: ExpresionesParser.ForStatementContext):
        self.tabla.push_scope()
        self.visit(ctx.forInit())
        iteracion = 0
        while bool(self.visit(ctx.expr())):
            iteracion += 1
            print(f"  [FOR] iteración {iteracion}")
            self.visit(ctx.block())
            self.visit(ctx.forUpdate())
        self.tabla.pop_scope()

    def visitForInitDecl(self, ctx: ExpresionesParser.ForInitDeclContext):
        tipo   = ctx.t_type().getText()
        nombre = ctx.ID().getText()
        valor  = self.convertir(self.visit(ctx.expr()), tipo)
        self.tabla.declarar_variable(nombre, tipo, valor)

    def visitForInitAssign(self, ctx: ExpresionesParser.ForInitAssignContext):
        nombre = ctx.ID().getText()
        tipo   = self.tabla.obtener_tipo(nombre)
        valor  = self.convertir(self.visit(ctx.expr()), tipo)
        self.tabla.asignar(nombre, valor)

    def visitForUpdate(self, ctx: ExpresionesParser.ForUpdateContext):
        nombre = ctx.ID().getText()
        tipo   = self.tabla.obtener_tipo(nombre)
        valor  = self.convertir(self.visit(ctx.expr()), tipo)
        self.tabla.asignar(nombre, valor)

    def visitReturnStatement(self, ctx: ExpresionesParser.ReturnStatementContext):
        valor = self.visit(ctx.expr()) if ctx.expr() else None
        raise ReturnSignal(valor)

    def visitPrintStatement(self, ctx: ExpresionesParser.PrintStatementContext):
        valor = self.visit(ctx.expr())
        print(valor)     # ← salida estándar del programa del usuario
        return valor

    def visitExprStatement(self, ctx: ExpresionesParser.ExprStatementContext):
        return self.visit(ctx.expr())

    def visitBlock(self, ctx: ExpresionesParser.BlockContext):
        return self.visitChildren(ctx)

    # ──────────────────────────────────────────────────────────
    # LLAMADA A FUNCIÓN
    # ──────────────────────────────────────────────────────────

    def visitFuncCallExpr(self, ctx: ExpresionesParser.FuncCallExprContext):
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

        # Crear nuevo scope para la función
        self.tabla.push_scope()

        # Ligar parámetros con los valores de los argumentos
        for (tipo_p, nombre_p), val in zip(params, args_vals):
            self.tabla.declarar_variable(nombre_p, tipo_p,
                                         self.convertir(val, tipo_p))

        # Ejecutar cuerpo de la función
        resultado = None
        try:
            self.visit(func_ctx.block())
        except ReturnSignal as r:
            resultado = r.valor

        # Salir del scope de la función
        self.tabla.pop_scope()
        return resultado

    # ──────────────────────────────────────────────────────────
    # EXPRESIONES ARITMÉTICAS Y LÓGICAS
    # ──────────────────────────────────────────────────────────

    def visitMulExpr(self, ctx: ExpresionesParser.MulExprContext):
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
            return izq % der

    def visitAddExpr(self, ctx: ExpresionesParser.AddExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()
        return izq + der if op == '+' else izq - der

    def visitRelExpr(self, ctx: ExpresionesParser.RelExprContext):
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

    def visitAndExpr(self, ctx: ExpresionesParser.AndExprContext):
        return bool(self.visit(ctx.expr(0))) and bool(self.visit(ctx.expr(1)))

    def visitOrExpr(self, ctx: ExpresionesParser.OrExprContext):
        return bool(self.visit(ctx.expr(0))) or bool(self.visit(ctx.expr(1)))

    def visitNotExpr(self, ctx: ExpresionesParser.NotExprContext):
        return not bool(self.visit(ctx.expr()))

    def visitNegExpr(self, ctx: ExpresionesParser.NegExprContext):
        return -self.visit(ctx.expr())

    def visitParenExpr(self, ctx: ExpresionesParser.ParenExprContext):
        return self.visit(ctx.expr())

    # ──────────────────────────────────────────────────────────
    # LITERALES
    # ──────────────────────────────────────────────────────────

    def visitNumExpr(self, ctx: ExpresionesParser.NumExprContext):
        return int(ctx.NUM().getText())

    def visitFloatExpr(self, ctx: ExpresionesParser.FloatExprContext):
        return float(ctx.FLOAT_LIT().getText())

    def visitBoolExpr(self, ctx: ExpresionesParser.BoolExprContext):
        return ctx.BOOL_LIT().getText() == 'true'

    def visitStringExpr(self, ctx: ExpresionesParser.StringExprContext):
        return ctx.STRING_LIT().getText()[1:-1]  # quitar comillas " "

    def visitIdExpr(self, ctx: ExpresionesParser.IdExprContext):
        nombre = ctx.ID().getText()
        simbolo = self.tabla.buscar(nombre)
        if simbolo is None:
            raise Exception(
                f"[Error] Variable '{nombre}' no fue declarada."
            )
        return simbolo['valor']

    # ──────────────────────────────────────────────────────────
    # CONVERSIÓN DE TIPOS
    # ──────────────────────────────────────────────────────────

    def convertir(self, valor, tipo: str):
        if tipo == 'int':    return int(valor)   if valor is not None else 0
        if tipo == 'float':  return float(valor) if valor is not None else 0.0
        if tipo == 'bool':   return bool(valor)
        if tipo == 'string': return str(valor)   if valor is not None else ''
        return valor