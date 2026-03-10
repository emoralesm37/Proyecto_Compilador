# ================================================================
# EvaluadorVisitor.py
# Visitor que evalúa expresiones del lenguaje Expresiones
# Hereda de ExpresionesVisitor (generado por ANTLR4)
# ================================================================
print(">>> DEBUG: Cargando EvaluadorVisitor CORRECTO <<<")

from antlr4 import *
from ExpresionesParser  import ExpresionesParser
from ExpresionesVisitor import ExpresionesVisitor

# se comentará la sugerencia del sistema.
class EvaluadorVisitor(ExpresionesVisitor):   

    def __init__(self):
        print(">>> DEBUG: __init__ de EvaluadorVisitor <<<")
        # Tabla de símbolos: { nombre_variable: valor }
        self.variables = {}
        # Tabla de tipos:    { nombre_variable: tipo  }
        self.tipos = {}

    # ============================================================
    # PROGRAMA PRINCIPAL
    # ============================================================
    def visitProgram(self, ctx: ExpresionesParser.ProgramContext):
        print(">>> DEBUG: visitProgram de EvaluadorVisitor LLAMADO <<<")
        print("=" * 50)
        print("  Iniciando ejecución del programa")
        print("=" * 50)
        self.visitChildren(ctx)
        print("\n" + "=" * 50)
        print("  Fin del programa")
        print("=" * 50)
        print("\n📊 Estado final de variables:")
        if self.variables:
            for nombre, valor in self.variables.items():
                print(f"   {self.tipos[nombre]:8} {nombre:10} = {valor}")
        else:
            print("   (sin variables declaradas)")

    # ============================================================
    # DECLARACIÓN DE VARIABLE: int x;
    # ============================================================
    def visitVarDecl(self, ctx: ExpresionesParser.VarDeclContext):
        tipo   = ctx.type_().getText()
        nombre = ctx.ID().getText()

        if nombre in self.variables:
            raise Exception(f"[Error Semántico] La variable '{nombre}' ya fue declarada.")

        # Valor inicial por defecto según el tipo
        valores_default = {
            'int':    0,
            'float':  0.0,
            'bool':   False,
            'string': ""
        }
        self.variables[nombre] = valores_default.get(tipo, None)
        self.tipos[nombre]     = tipo
        print(f"  [Declaración] {tipo} {nombre} -> valor inicial: {self.variables[nombre]}")

    # ============================================================
    # ASIGNACIÓN: x = expr;
    # ============================================================
    def visitAssignment(self, ctx: ExpresionesParser.AssignmentContext):
        nombre = ctx.ID().getText()

        if nombre not in self.variables:
            raise Exception(f"[Error Semántico] Variable '{nombre}' no declarada.")

        valor = self.visit(ctx.expr())

        # Conversión de tipo básica según el tipo declarado
        tipo = self.tipos[nombre]
        if tipo == 'int':
            valor = int(valor)
        elif tipo == 'float':
            valor = float(valor)
        elif tipo == 'bool':
            valor = bool(valor)

        self.variables[nombre] = valor
        print(f"  [Asignación]  {nombre} = {valor}")
        return valor

    # ============================================================
    # EXPRESIÓN COMO SENTENCIA: expr;
    # ============================================================
    def visitExprStatement(self, ctx: ExpresionesParser.ExprStatementContext):
        resultado = self.visit(ctx.expr())
        print(f"  [Expresión]   resultado -> {resultado}")
        return resultado

    # ============================================================
    # CONDICIONAL: if (expr) bloque [else bloque]
    # ============================================================
    def visitIfStatement(self, ctx: ExpresionesParser.IfStatementContext):
        condicion = self.visit(ctx.expr())
        print(f"  [IF]          condición evaluada -> {condicion}")

        if condicion:
            print("  [IF]          ejecutando rama TRUE")
            self.visit(ctx.block(0))
        elif ctx.ELSE() is not None:
            print("  [IF]          ejecutando rama ELSE")
            self.visit(ctx.block(1))
        else:
            print("  [IF]          condición falsa, sin rama ELSE")

    # ============================================================
    # BLOQUE DE CÓDIGO: { statements* }
    # ============================================================
    def visitBlock(self, ctx: ExpresionesParser.BlockContext):
        return self.visitChildren(ctx)

    # ============================================================
    # EXPRESIONES LÓGICAS
    # ============================================================

    def visitOrExpr(self, ctx: ExpresionesParser.OrExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        return bool(izq) or bool(der)

    def visitAndExpr(self, ctx: ExpresionesParser.AndExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        return bool(izq) and bool(der)

    def visitNotExpr(self, ctx: ExpresionesParser.NotExprContext):
        valor = self.visit(ctx.expr())
        return not bool(valor)

    # ============================================================
    # EXPRESIONES RELACIONALES: ==, !=, <>, <, >, <=, >=
    # ============================================================
    def visitRelExpr(self, ctx: ExpresionesParser.RelExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()

        operaciones = {
            '==': lambda a, b: a == b,
            '!=': lambda a, b: a != b,
            '<>': lambda a, b: a != b,
            '<' : lambda a, b: a <  b,
            '>' : lambda a, b: a >  b,
            '<=': lambda a, b: a <= b,
            '>=': lambda a, b: a >= b,
        }

        if op not in operaciones:
            raise Exception(f"[Error] Operador relacional desconocido: '{op}'")

        return operaciones[op](izq, der)

    # ============================================================
    # EXPRESIONES ARITMÉTICAS
    # ============================================================

    def visitAddExpr(self, ctx: ExpresionesParser.AddExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()

        if op == '+':
            return izq + der
        elif op == '-':
            return izq - der

    def visitMulExpr(self, ctx: ExpresionesParser.MulExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()

        if op == '*':
            return izq * der
        elif op == '/':
            if der == 0:
                raise Exception("[Error Semántico] División por cero no permitida.")
            # División entera para int/int, decimal si hay float
            if isinstance(izq, float) or isinstance(der, float):
                return izq / der
            return izq // der

    # ============================================================
    # NEGACIÓN ARITMÉTICA UNARIA: -expr
    # ============================================================
    def visitNegExpr(self, ctx: ExpresionesParser.NegExprContext):
        valor = self.visit(ctx.expr())
        return -valor

    # ============================================================
    # AGRUPACIÓN: (expr)
    # ============================================================
    def visitParenExpr(self, ctx: ExpresionesParser.ParenExprContext):
        return self.visit(ctx.expr())

    # ============================================================
    # LITERALES
    # ============================================================

    def visitNumExpr(self, ctx: ExpresionesParser.NumExprContext):
        return int(ctx.NUM().getText())

    def visitFloatExpr(self, ctx: ExpresionesParser.FloatExprContext):
        return float(ctx.FLOAT_LIT().getText())

    def visitBoolExpr(self, ctx: ExpresionesParser.BoolExprContext):
        return ctx.BOOL_LIT().getText() == 'true'

    # ============================================================
    # IDENTIFICADOR (lectura de variable)
    # ============================================================
    def visitIdExpr(self, ctx: ExpresionesParser.IdExprContext):
        nombre = ctx.ID().getText()
        if nombre not in self.variables:
            raise Exception(f"[Error Semántico] Variable '{nombre}' usada antes de ser declarada.")
        return self.variables[nombre]