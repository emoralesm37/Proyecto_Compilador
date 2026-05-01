# ================================================================
# semantic_visitor.py
# Visitor Semántico — Type Checking y validación de ámbitos
# NO ejecuta código, SOLO valida
# ================================================================

from antlr4 import *
from gramatica_v3Parser  import gramatica_v3Parser
from gramatica_v3Visitor  import gramatica_v3Visitor
from Tabla_de_simbolos  import TablaSimbolos

def visitProgram(self, ctx: gramatica_v3Parser.ProgramContext):
    #obtener el nombre dle programa
    if ctx.ID():
        nombre_programa = ctx.ID().getText()
    else:
        nombre_programa = "Programa sin nombre" # solo si no se especifica un nombre

    print("=" * 55)
    print(f"  Iniciando ejecución de '{nombre_programa}'")
    print("=" * 55 + "\n")

class SemanticVisitor(gramatica_v3Visitor):

    def __init__(self):
        self.tabla            = TablaSimbolos()
        self.errores          = []
        self.funcion_actual   = None   # nombre de la función en curso
        self.retorno_actual   = None   # tipo de retorno esperado

    # ──────────────────────────────────────────────────────────
    # UTILIDADES
    # ──────────────────────────────────────────────────────────

    def error(self, msg: str, token=None):
        if token:
            linea  = token.line
            col    = token.column
            self.errores.append(
                f"[Error Semántico] Línea {linea}, Columna {col}: {msg}"
            )
        else:
            self.errores.append(f"[Error Semántico] {msg}")

    def hay_errores(self):
        return len(self.errores) > 0

    def tipos_compatibles(self, tipo_destino: str, tipo_origen: str) -> bool:
        """int y float son compatibles entre sí; el resto debe ser idéntico."""
        if tipo_destino == tipo_origen:
            return True
        numericos = {'int', 'float'}
        return tipo_destino in numericos and tipo_origen in numericos

    def tipo_aritmetico(self, t1, t2):
        """float si alguno es float, int si ambos son int."""
        if t1 == 'float' or t2 == 'float':
            return 'float'
        if t1 == 'int' and t2 == 'int':
            return 'int'
        return None

    # ──────────────────────────────────────────────────────────
    # PROGRAMA — dos pasadas para soportar forward references
    # ──────────────────────────────────────────────────────────

    def visitProgram(self, ctx: gramatica_v3Parser.ProgramContext):
        # Pasada 1: registrar todas las funciones
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v3Parser.TopFuncDeclContext):
                self._registrar_funcion(decl.funcDecl())

        # Pasada 2: validar cuerpos y sentencias
        for decl in ctx.topLevelDecl():
            self.visit(decl)

    def _registrar_funcion(self, ctx: gramatica_v3Parser.FuncDeclContext):
        """Registra solo la firma de la función (sin visitar el cuerpo)."""
        nombre       = ctx.ID().getText()
        tipo_retorno = ctx.returnType().getText()
        token        = ctx.ID().getSymbol()

        parametros = []
        if ctx.paramList():
            for p in ctx.paramList().param():
                parametros.append((p.t_type().getText(), p.ID().getText()))

        try:
            self.tabla.declarar_funcion(nombre, tipo_retorno, parametros,
                                        token.line, token.column)
        except Exception as e:
            self.error(str(e))

    # ──────────────────────────────────────────────────────────
    # DECLARACIONES DE NIVEL SUPERIOR
    # ──────────────────────────────────────────────────────────

    def visitTopFuncDecl(self, ctx: gramatica_v3Parser.TopFuncDeclContext):
        self._validar_cuerpo_funcion(ctx.funcDecl())

    def visitTopStatement(self, ctx: gramatica_v3Parser.TopStatementContext):
        self.visit(ctx.statement())

    def _validar_cuerpo_funcion(self, ctx: gramatica_v3Parser.FuncDeclContext):
        nombre       = ctx.ID().getText()
        tipo_retorno = ctx.returnType().getText()

        # Entrar al ámbito de la función
        self.tabla.push_scope()
        func_previa    = self.funcion_actual
        retorno_previo = self.retorno_actual
        self.funcion_actual = nombre
        self.retorno_actual = tipo_retorno

        # Declarar parámetros en el ámbito local
        if ctx.paramList():
            for p in ctx.paramList().param():
                tipo_p   = p.t_type().getText()
                nombre_p = p.ID().getText()
                token_p  = p.ID().getSymbol()
                try:
                    self.tabla.declarar_variable(nombre_p, tipo_p,
                                                 linea=token_p.line,
                                                 columna=token_p.column)
                except Exception as e:
                    self.error(str(e))

        # Validar cuerpo
        self.visit(ctx.block())

        # Salir del ámbito
        self.tabla.pop_scope()
        self.funcion_actual = func_previa
        self.retorno_actual = retorno_previo

    # ──────────────────────────────────────────────────────────
    # SENTENCIAS
    # ──────────────────────────────────────────────────────────

    def visitVarDecl(self, ctx: gramatica_v3Parser.VarDeclContext):
        tipo = ctx.t_type().getText()
        nombre = ctx.ID().getText()
        token  = ctx.ID().getSymbol()

        # Verificar inicializador
        if ctx.expr():
            tipo_expr = self.tipo_expr(ctx.expr())
            if tipo_expr and not self.tipos_compatibles(tipo, tipo_expr):
                self.error(
                    f"Incompatibilidad de tipos. "
                    f"No se puede asignar '{tipo_expr}' a '{tipo}'.",
                    token
                )

        try:
            self.tabla.declarar_variable(nombre, tipo,
                                         linea=token.line,
                                         columna=token.column)
        except Exception as e:
            self.error(str(e))

    def visitAssignment(self, ctx: gramatica_v3Parser.AssignmentContext):
        nombre = ctx.ID().getText()
        token  = ctx.ID().getSymbol()

        simbolo = self.tabla.buscar(nombre)
        if simbolo is None:
            self.error(f"Variable '{nombre}' no fue declarada.", token)
            return

        tipo_var  = simbolo['tipo']
        tipo_expr = self.tipo_expr(ctx.expr())

        if tipo_expr and not self.tipos_compatibles(tipo_var, tipo_expr):
            self.error(
                f"Incompatibilidad de tipos. "
                f"No se puede asignar '{tipo_expr}' a '{tipo_var}'.",
                token
            )

    def visitIfStatement(self, ctx: gramatica_v3Parser.IfStatementContext):
        self.tipo_expr(ctx.expr())   # validar condición

        self.tabla.push_scope()
        self.visit(ctx.block(0))
        self.tabla.pop_scope()

        if ctx.ELSE():
            self.tabla.push_scope()
            self.visit(ctx.block(1))
            self.tabla.pop_scope()

    def visitWhileStatement(self, ctx: gramatica_v3Parser.WhileStatementContext):
        self.tipo_expr(ctx.expr())

        self.tabla.push_scope()
        self.visit(ctx.block())
        self.tabla.pop_scope()

    def visitForStatement(self, ctx: gramatica_v3Parser.ForStatementContext):
        self.tabla.push_scope()
        self.visit(ctx.forInit())
        self.tipo_expr(ctx.expr())
        self.visit(ctx.forUpdate())
        self.visit(ctx.block())
        self.tabla.pop_scope()

    def visitForInitDecl(self, ctx: gramatica_v3Parser.ForInitDeclContext):
        tipo   = ctx.t_type().getText()
        nombre = ctx.ID().getText()
        token  = ctx.ID().getSymbol()
        tipo_expr = self.tipo_expr(ctx.expr())

        if tipo_expr and not self.tipos_compatibles(tipo, tipo_expr):
            self.error(
                f"Incompatibilidad en inicialización del for: "
                f"'{tipo_expr}' a '{tipo}'.", token
            )
        try:
            self.tabla.declarar_variable(nombre, tipo,
                                         linea=token.line,
                                         columna=token.column)
        except Exception as e:
            self.error(str(e))

    def visitForInitAssign(self, ctx: gramatica_v3Parser.ForInitAssignContext):
        nombre = ctx.ID().getText()
        token  = ctx.ID().getSymbol()
        if not self.tabla.buscar(nombre):
            self.error(f"Variable '{nombre}' no fue declarada.", token)

    def visitForUpdate(self, ctx: gramatica_v3Parser.ForUpdateContext):
        nombre = ctx.ID().getText()
        token  = ctx.ID().getSymbol()
        if not self.tabla.buscar(nombre):
            self.error(f"Variable '{nombre}' no fue declarada.", token)

    def visitReturnStatement(self, ctx: gramatica_v3Parser.ReturnStatementContext):
        token = ctx.RETURN().getSymbol()

        if self.funcion_actual is None:
            self.error("'return' usado fuera de una función.", token)
            return

        if ctx.expr():
            tipo_ret = self.tipo_expr(ctx.expr())
            if (tipo_ret and self.retorno_actual != 'void'
                    and not self.tipos_compatibles(self.retorno_actual, tipo_ret)):
                self.error(
                    f"Tipo de retorno incorrecto en función "
                    f"'{self.funcion_actual}': "
                    f"se esperaba '{self.retorno_actual}' "
                    f"pero se retorna '{tipo_ret}'.",
                    token
                )
        elif self.retorno_actual != 'void':
            self.error(
                f"La función '{self.funcion_actual}' debe retornar "
                f"un valor de tipo '{self.retorno_actual}'.",
                token
            )

    def visitPrintStatement(self, ctx: gramatica_v3Parser.PrintStatementContext):
        self.tipo_expr(ctx.expr())   # solo valida que sea una expresión válida

    def visitExprStatement(self, ctx: gramatica_v3Parser.ExprStatementContext):
        self.tipo_expr(ctx.expr())

    def visitBlock(self, ctx: gramatica_v3Parser.BlockContext):
        return self.visitChildren(ctx)

    # ──────────────────────────────────────────────────────────
    # INFERENCIA DE TIPOS DE EXPRESIONES
    # ──────────────────────────────────────────────────────────

    def tipo_expr(self, ctx) -> str | None:
        """Infiere el tipo de una expresión y valida semánticamente."""
        if ctx is None:
            return None

        clase = type(ctx).__name__

        if clase == 'NumExprContext':
            return 'int'

        elif clase == 'FloatExprContext':
            return 'float'

        elif clase == 'BoolExprContext':
            return 'bool'

        elif clase == 'StringExprContext':
            return 'string'

        elif clase == 'IdExprContext':
            nombre = ctx.ID().getText()
            token  = ctx.ID().getSymbol()
            simbolo = self.tabla.buscar(nombre)
            if simbolo is None:
                self.error(
                    f"Variable '{nombre}' usada sin ser declarada.", token
                )
                return None
            return simbolo['tipo']

        elif clase == 'MulExprContext':
            t1 = self.tipo_expr(ctx.expr(0))
            t2 = self.tipo_expr(ctx.expr(1))
            return self.tipo_aritmetico(t1, t2)

        elif clase == 'AddExprContext':
            t1 = self.tipo_expr(ctx.expr(0))
            t2 = self.tipo_expr(ctx.expr(1))
            op = ctx.getChild(1).getText()
            # Permitir concatenación de strings con +
            if op == '+' and t1 == 'string' and t2 == 'string':
                return 'string'
            return self.tipo_aritmetico(t1, t2)

        elif clase in ('RelExprContext', 'AndExprContext',
                       'OrExprContext', 'NotExprContext'):
            # Validar sub-expresiones aunque el resultado sea bool
            if hasattr(ctx, 'expr'):
                for i in range(ctx.getChildCount()):
                    child = ctx.getChild(i)
                    if hasattr(child, 'getRuleIndex'):
                        self.tipo_expr(child)
            return 'bool'

        elif clase == 'NegExprContext':
            return self.tipo_expr(ctx.expr())

        elif clase == 'ParenExprContext':
            return self.tipo_expr(ctx.expr())

        elif clase == 'FuncCallExprContext':
            return self._validar_llamada(ctx)

        return None

    def _validar_llamada(self, ctx: gramatica_v3Parser.FuncCallExprContext):
        """Valida una llamada a función y retorna su tipo de retorno."""
        nombre = ctx.ID().getText()
        token  = ctx.ID().getSymbol()

        func = self.tabla.buscar_funcion(nombre)
        if func is None:
            self.error(f"Función '{nombre}' no fue declarada.", token)
            return None

        # Validar cantidad de argumentos
        args   = ctx.argList().expr() if ctx.argList() else []
        params = func['parametros']

        if len(args) != len(params):
            self.error(
                f"Función '{nombre}' espera {len(params)} argumento(s) "
                f"pero se pasaron {len(args)}.",
                token
            )
            return func['tipo_retorno']

        # Validar tipos de argumentos
        for i, (arg, (tipo_param, nombre_param)) in enumerate(
                zip(args, params)):
            tipo_arg = self.tipo_expr(arg)
            if tipo_arg and not self.tipos_compatibles(tipo_param, tipo_arg):
                self.error(
                    f"Argumento {i+1} de '{nombre}': "
                    f"se esperaba '{tipo_param}' "
                    f"pero se pasó '{tipo_arg}'.",
                    token
                )

        return func['tipo_retorno']