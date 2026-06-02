# ================================================================
# semantic_visitor_v4.py
# Visitor Semántico v4 — Type Checking y validación de ámbitos
# Novedades: switch/case, operador ternario, cast explícito, structs
# NO ejecuta código, SOLO valida
# ================================================================

from antlr4 import *
from gramatica_v4Parser  import gramatica_v4Parser
from gramatica_v4Visitor import gramatica_v4Visitor
from Tabla_de_simbolos   import TablaSimbolos


class SemanticVisitor(gramatica_v4Visitor):

    def __init__(self):
        self.tabla          = TablaSimbolos()
        self.errores        = []
        self.funcion_actual = None   # nombre de la función en curso
        self.retorno_actual = None   # tipo de retorno esperado
        # Registro de tipos struct: nombre → {campo: tipo}
        self.structs: dict[str, dict[str, str]] = {}
        # Pila para controlar si estamos dentro de un switch (break válido)
        self._dentro_switch = 0
        # Pila para controlar si estamos dentro de un ciclo (break/continue)
        self._dentro_ciclo  = 0

    # ──────────────────────────────────────────────────────────
    # UTILIDADES
    # ──────────────────────────────────────────────────────────

    def error(self, msg: str, token=None):
        if token:
            self.errores.append(
                f"[Error Semántico] Línea {token.line}, "
                f"Columna {token.column}: {msg}"
            )
        else:
            self.errores.append(f"[Error Semántico] {msg}")

    def hay_errores(self) -> bool:
        return len(self.errores) > 0

    def tipos_compatibles(self, tipo_destino: str, tipo_origen: str) -> bool:
        if tipo_destino == tipo_origen:
            return True
        numericos = {'int', 'float'}
        return tipo_destino in numericos and tipo_origen in numericos

    def tipo_aritmetico(self, t1, t2):
        if t1 == 'float' or t2 == 'float':
            return 'float'
        if t1 == 'int' and t2 == 'int':
            return 'int'
        return None

    # ──────────────────────────────────────────────────────────
    # PROGRAMA — dos pasadas
    # ──────────────────────────────────────────────────────────

    def visitProgram(self, ctx: gramatica_v4Parser.ProgramContext):
        # Pasada 1: registrar structs y funciones (forward references)
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v4Parser.TopStructDeclContext):
                self._registrar_struct(decl.structDecl())
            elif isinstance(decl, gramatica_v4Parser.TopFuncDeclContext):
                self._registrar_funcion(decl.funcDecl())

        # Pasada 2: validar cuerpos y sentencias
        for decl in ctx.topLevelDecl():
            self.visit(decl)

    def _registrar_struct(self, ctx: gramatica_v4Parser.StructDeclContext):
        nombre = ctx.ID().getText()
        token  = ctx.ID().getSymbol()

        if nombre in self.structs:
            self.error(f"Struct '{nombre}' ya fue declarado.", token)
            return

        campos = {}
        for campo in ctx.structField():
            tipo_campo   = campo.t_type().getText()
            nombre_campo = campo.ID().getText()
            if nombre_campo in campos:
                self.error(
                    f"Campo '{nombre_campo}' duplicado en struct '{nombre}'.",
                    campo.ID().getSymbol()
                )
            campos[nombre_campo] = tipo_campo

        self.structs[nombre] = campos

    def _registrar_funcion(self, ctx: gramatica_v4Parser.FuncDeclContext):
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

    def visitTopStructDecl(self, ctx: gramatica_v4Parser.TopStructDeclContext):
        pass   # ya registrado en la pasada 1

    def visitTopFuncDecl(self, ctx: gramatica_v4Parser.TopFuncDeclContext):
        self._validar_cuerpo_funcion(ctx.funcDecl())

    def visitTopImport(self, ctx: gramatica_v4Parser.TopImportContext):
        pass   # imports no se validan semánticamente

    def visitTopStatement(self, ctx: gramatica_v4Parser.TopStatementContext):
        self.visit(ctx.statement())

    def _validar_cuerpo_funcion(self, ctx: gramatica_v4Parser.FuncDeclContext):
        nombre       = ctx.ID().getText()
        tipo_retorno = ctx.returnType().getText()

        self.tabla.push_scope()
        func_previa    = self.funcion_actual
        retorno_previo = self.retorno_actual
        self.funcion_actual = nombre
        self.retorno_actual = tipo_retorno

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

        self.visit(ctx.block())
        self.tabla.pop_scope()
        self.funcion_actual = func_previa
        self.retorno_actual = retorno_previo

    # ──────────────────────────────────────────────────────────
    # SENTENCIAS
    # ──────────────────────────────────────────────────────────

    def visitVarDecl(self, ctx: gramatica_v4Parser.VarDeclContext):
        tipo   = ctx.t_type().getText()
        nombre = ctx.ID().getText()
        token  = ctx.ID().getSymbol()

        if ctx.expr():
            tipo_expr = self.tipo_expr(ctx.expr())
            if tipo_expr and not self.tipos_compatibles(tipo, tipo_expr):
                self.error(
                    f"Incompatibilidad de tipos: no se puede asignar "
                    f"'{tipo_expr}' a '{tipo}'.", token
                )
        try:
            self.tabla.declarar_variable(nombre, tipo,
                                         linea=token.line,
                                         columna=token.column)
        except Exception as e:
            self.error(str(e))

    def visitArrayDecl(self, ctx: gramatica_v4Parser.ArrayDeclContext):
        texto_tipo = ctx.arrayType().getText()
        nombre     = ctx.ID().getText()
        token      = ctx.ID().getSymbol()
        try:
            self.tabla.declarar_variable(nombre, texto_tipo,
                                         linea=token.line,
                                         columna=token.column)
        except Exception as e:
            self.error(str(e))

    def visitStructVarDecl(self, ctx: gramatica_v4Parser.StructVarDeclContext):
        """Declaración de variable de tipo struct: Punto p;"""
        tipo_struct  = ctx.ID(0).getText()
        nombre_var   = ctx.ID(1).getText()
        token_tipo   = ctx.ID(0).getSymbol()
        token_var    = ctx.ID(1).getSymbol()

        if tipo_struct not in self.structs:
            self.error(
                f"Tipo struct '{tipo_struct}' no fue declarado.", token_tipo
            )
        try:
            self.tabla.declarar_variable(nombre_var, tipo_struct,
                                         linea=token_var.line,
                                         columna=token_var.column)
        except Exception as e:
            self.error(str(e))

    def visitAssignment(self, ctx: gramatica_v4Parser.AssignmentContext):
        nombre = ctx.ID().getText()
        token  = ctx.ID().getSymbol()
        simbolo = self.tabla.buscar(nombre)
        if simbolo is None:
            self.error(f"Variable '{nombre}' no fue declarada.", token)
            return
        tipo_expr = self.tipo_expr(ctx.expr())
        if tipo_expr and not self.tipos_compatibles(simbolo['tipo'], tipo_expr):
            self.error(
                f"Incompatibilidad: no se puede asignar '{tipo_expr}' "
                f"a '{simbolo['tipo']}'.", token
            )

    def visitFieldAssign(self, ctx: gramatica_v4Parser.FieldAssignContext):
        """Validación de p.x = expr;"""
        nombre_var   = ctx.ID(0).getText()
        nombre_campo = ctx.ID(1).getText()
        token        = ctx.ID(0).getSymbol()

        simbolo = self.tabla.buscar(nombre_var)
        if simbolo is None:
            self.error(f"Variable '{nombre_var}' no fue declarada.", token)
            return

        tipo_struct = simbolo['tipo']
        if tipo_struct not in self.structs:
            self.error(
                f"'{nombre_var}' no es de tipo struct (es '{tipo_struct}').",
                token
            )
            return

        campos = self.structs[tipo_struct]
        if nombre_campo not in campos:
            self.error(
                f"El struct '{tipo_struct}' no tiene un campo '{nombre_campo}'.",
                ctx.ID(1).getSymbol()
            )
            return

        tipo_campo = campos[nombre_campo]
        tipo_valor = self.tipo_expr(ctx.expr())
        if tipo_valor and not self.tipos_compatibles(tipo_campo, tipo_valor):
            self.error(
                f"Campo '{nombre_campo}' es de tipo '{tipo_campo}', "
                f"pero se asigna '{tipo_valor}'.", token
            )

    def visitArrayAssign(self, ctx: gramatica_v4Parser.ArrayAssignContext):
        nombre = ctx.ID().getText()
        token  = ctx.ID().getSymbol()
        if not self.tabla.buscar(nombre):
            self.error(f"Variable '{nombre}' no fue declarada.", token)
        self.tipo_expr(ctx.expr(0))
        self.tipo_expr(ctx.expr(1))

    def visitIfStatement(self, ctx: gramatica_v4Parser.IfStatementContext):
        self.tipo_expr(ctx.expr())
        self.tabla.push_scope()
        self.visit(ctx.block(0))
        self.tabla.pop_scope()
        if ctx.ELSE():
            self.tabla.push_scope()
            self.visit(ctx.block(1))
            self.tabla.pop_scope()

    def visitWhileStatement(self, ctx: gramatica_v4Parser.WhileStatementContext):
        self.tipo_expr(ctx.expr())
        self._dentro_ciclo += 1
        self.tabla.push_scope()
        self.visit(ctx.block())
        self.tabla.pop_scope()
        self._dentro_ciclo -= 1

    def visitForStatement(self, ctx: gramatica_v4Parser.ForStatementContext):
        self.tabla.push_scope()
        self.visit(ctx.forInit())
        self.tipo_expr(ctx.expr())
        self.visit(ctx.forUpdate())
        self._dentro_ciclo += 1
        self.visit(ctx.block())
        self._dentro_ciclo -= 1
        self.tabla.pop_scope()

    def visitSwitchStatement(self, ctx: gramatica_v4Parser.SwitchStatementContext):
        """Validación de switch(expr) { case v: ...; default: ...; }"""
        tipo_control = self.tipo_expr(ctx.expr())

        self._dentro_switch += 1
        self.tabla.push_scope()

        for case_clause in ctx.caseClause():
            tipo_case = self.tipo_expr(case_clause.expr())
            # El tipo del case debe ser compatible con el tipo de control
            if tipo_control and tipo_case and \
               not self.tipos_compatibles(tipo_control, tipo_case):
                token = case_clause.expr().start
                self.error(
                    f"El valor del case '{tipo_case}' no es compatible "
                    f"con el tipo de control '{tipo_control}'.", token
                )
            for stmt in case_clause.statement():
                self.visit(stmt)

        if ctx.defaultClause():
            for stmt in ctx.defaultClause().statement():
                self.visit(stmt)

        self.tabla.pop_scope()
        self._dentro_switch -= 1

    def visitForInitDecl(self, ctx: gramatica_v4Parser.ForInitDeclContext):
        tipo   = ctx.t_type().getText()
        nombre = ctx.ID().getText()
        token  = ctx.ID().getSymbol()
        tipo_expr = self.tipo_expr(ctx.expr())
        if tipo_expr and not self.tipos_compatibles(tipo, tipo_expr):
            self.error(
                f"Incompatibilidad en init del for: '{tipo_expr}' a '{tipo}'.",
                token
            )
        try:
            self.tabla.declarar_variable(nombre, tipo,
                                         linea=token.line,
                                         columna=token.column)
        except Exception as e:
            self.error(str(e))

    def visitForInitAssign(self, ctx: gramatica_v4Parser.ForInitAssignContext):
        nombre = ctx.ID().getText()
        token  = ctx.ID().getSymbol()
        if not self.tabla.buscar(nombre):
            self.error(f"Variable '{nombre}' no fue declarada.", token)

    def visitForUpdate(self, ctx: gramatica_v4Parser.ForUpdateContext):
        nombre = ctx.ID().getText()
        token  = ctx.ID().getSymbol()
        if not self.tabla.buscar(nombre):
            self.error(f"Variable '{nombre}' no fue declarada.", token)

    def visitReturnStatement(self, ctx: gramatica_v4Parser.ReturnStatementContext):
        token = ctx.RETURN().getSymbol()
        if self.funcion_actual is None:
            self.error("'return' usado fuera de una función.", token)
            return
        if ctx.expr():
            tipo_ret = self.tipo_expr(ctx.expr())
            if (tipo_ret and self.retorno_actual != 'void'
                    and not self.tipos_compatibles(self.retorno_actual, tipo_ret)):
                self.error(
                    f"Tipo de retorno incorrecto en '{self.funcion_actual}': "
                    f"se esperaba '{self.retorno_actual}' "
                    f"pero se retorna '{tipo_ret}'.", token
                )
        elif self.retorno_actual != 'void':
            self.error(
                f"La función '{self.funcion_actual}' debe retornar "
                f"'{self.retorno_actual}'.", token
            )

    def visitBreakStatement(self, ctx: gramatica_v4Parser.BreakStatementContext):
        token = ctx.BREAK().getSymbol()
        if self._dentro_ciclo == 0 and self._dentro_switch == 0:
            self.error(
                "'break' usado fuera de un ciclo o switch.", token
            )

    def visitContinueStatement(self, ctx: gramatica_v4Parser.ContinueStatementContext):
        token = ctx.CONTINUE().getSymbol()
        if self._dentro_ciclo == 0:
            self.error("'continue' usado fuera de un ciclo.", token)

    def visitPrintStatement(self, ctx: gramatica_v4Parser.PrintStatementContext):
        self.tipo_expr(ctx.expr())

    def visitExprStatement(self, ctx: gramatica_v4Parser.ExprStatementContext):
        self.tipo_expr(ctx.expr())

    def visitBlock(self, ctx: gramatica_v4Parser.BlockContext):
        return self.visitChildren(ctx)

    # ──────────────────────────────────────────────────────────
    # INFERENCIA DE TIPOS DE EXPRESIONES
    # ──────────────────────────────────────────────────────────

    def tipo_expr(self, ctx) -> str | None:
        if ctx is None:
            return None

        clase = type(ctx).__name__

        # ── Literales ──
        if   clase == 'NumExprContext':    return 'int'
        elif clase == 'FloatExprContext':  return 'float'
        elif clase == 'BoolExprContext':   return 'bool'
        elif clase == 'StringExprContext': return 'string'

        # ── Identificador ──
        elif clase == 'IdExprContext':
            nombre  = ctx.ID().getText()
            token   = ctx.ID().getSymbol()
            simbolo = self.tabla.buscar(nombre)
            if simbolo is None:
                self.error(f"Variable '{nombre}' usada sin ser declarada.", token)
                return None
            return simbolo['tipo']

        # ── Aritmética ──
        elif clase == 'MulExprContext':
            t1 = self.tipo_expr(ctx.expr(0))
            t2 = self.tipo_expr(ctx.expr(1))
            return self.tipo_aritmetico(t1, t2)

        elif clase == 'AddExprContext':
            t1 = self.tipo_expr(ctx.expr(0))
            t2 = self.tipo_expr(ctx.expr(1))
            op = ctx.getChild(1).getText()
            if op == '+' and t1 == 'string' and t2 == 'string':
                return 'string'
            return self.tipo_aritmetico(t1, t2)

        # ── Lógica / Relacional ──
        elif clase in ('RelExprContext', 'AndExprContext',
                       'OrExprContext', 'NotExprContext'):
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if hasattr(child, 'getRuleIndex'):
                    self.tipo_expr(child)
            return 'bool'

        elif clase == 'NegExprContext':
            return self.tipo_expr(ctx.expr())

        elif clase == 'ParenExprContext':
            return self.tipo_expr(ctx.expr())

        # ── Operador Ternario (novedad v4): cond ? expr_v : expr_f ──
        elif clase == 'TernaryExprContext':
            t_cond  = self.tipo_expr(ctx.expr(0))
            t_verd  = self.tipo_expr(ctx.expr(1))
            t_falso = self.tipo_expr(ctx.expr(2))
            # Ambas ramas deben ser del mismo tipo (o numérico compatible)
            if t_verd and t_falso:
                if self.tipos_compatibles(t_verd, t_falso):
                    return 'float' if 'float' in (t_verd, t_falso) else t_verd
                else:
                    token = ctx.expr(1).start
                    self.error(
                        f"Las ramas del ternario tienen tipos incompatibles: "
                        f"'{t_verd}' y '{t_falso}'.", token
                    )
            return t_verd

        # ── Casting explícito (novedad v4): (tipo) expr ──
        elif clase == 'CastExprContext':
            tipo_destino = ctx.t_type().getText()
            tipo_origen  = self.tipo_expr(ctx.expr())
            tipos_validos = {'int', 'float', 'bool', 'string'}
            if tipo_origen and tipo_origen not in tipos_validos:
                token = ctx.t_type().start
                self.error(
                    f"No se puede hacer cast desde el tipo '{tipo_origen}'.",
                    token
                )
            return tipo_destino

        # ── Acceso a campo de struct (novedad v4): p.x ──
        elif clase == 'FieldAccessExprContext':
            nombre_var   = ctx.ID(0).getText()
            nombre_campo = ctx.ID(1).getText()
            token        = ctx.ID(0).getSymbol()

            simbolo = self.tabla.buscar(nombre_var)
            if simbolo is None:
                self.error(f"Variable '{nombre_var}' no fue declarada.", token)
                return None

            tipo_struct = simbolo['tipo']
            if tipo_struct not in self.structs:
                self.error(
                    f"'{nombre_var}' no es de tipo struct "
                    f"(tipo actual: '{tipo_struct}').", token
                )
                return None

            campos = self.structs[tipo_struct]
            if nombre_campo not in campos:
                self.error(
                    f"El struct '{tipo_struct}' no tiene campo '{nombre_campo}'.",
                    ctx.ID(1).getSymbol()
                )
                return None

            return campos[nombre_campo]

        # ── Acceso a arreglo: nums[i] ──
        elif clase == 'ArrayAccessExprContext':
            nombre = ctx.ID().getText()
            token  = ctx.ID().getSymbol()
            simbolo = self.tabla.buscar(nombre)
            if simbolo is None:
                self.error(f"Variable '{nombre}' no fue declarada.", token)
                return None
            self.tipo_expr(ctx.expr())
            tipo = simbolo['tipo']
            return tipo.replace('[]', '') if tipo.endswith('[]') else tipo

        # ── Llamada a función ──
        elif clase == 'FuncCallExprContext':
            return self._validar_llamada(ctx)

        return None

    def _validar_llamada(self, ctx: gramatica_v4Parser.FuncCallExprContext):
        nombre = ctx.ID().getText()
        token  = ctx.ID().getSymbol()

        func = self.tabla.buscar_funcion(nombre)
        if func is None:
            self.error(f"Función '{nombre}' no fue declarada.", token)
            return None

        args   = ctx.argList().expr() if ctx.argList() else []
        params = func['parametros']

        if len(args) != len(params):
            self.error(
                f"Función '{nombre}' espera {len(params)} argumento(s) "
                f"pero se pasaron {len(args)}.", token
            )
            return func['tipo_retorno']

        for i, (arg, (tipo_param, _)) in enumerate(zip(args, params)):
            tipo_arg = self.tipo_expr(arg)
            if tipo_arg and not self.tipos_compatibles(tipo_param, tipo_arg):
                self.error(
                    f"Argumento {i+1} de '{nombre}': "
                    f"se esperaba '{tipo_param}' pero se pasó '{tipo_arg}'.",
                    token
                )

        return func['tipo_retorno']
