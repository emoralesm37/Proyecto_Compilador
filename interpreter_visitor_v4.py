# ================================================================
# interpreter_visitor_v4.py
# Visitor Intérprete v4 — Ejecuta el AST validado
# Novedades: switch/case, operador ternario, cast explícito, structs
# ================================================================

from antlr4 import *
from gramatica_v4Parser  import gramatica_v4Parser
from gramatica_v4Visitor import gramatica_v4Visitor
from Tabla_de_simbolos   import TablaSimbolos


# ──────────────────────────────────────────────────────────────
# SEÑALES DE CONTROL DE FLUJO
# ──────────────────────────────────────────────────────────────

class ReturnSignal(Exception):
    """Propaga un valor de retorno desde una función."""
    def __init__(self, valor):
        self.valor = valor

class BreakSignal(Exception):
    """Sale del ciclo o switch más interno (break)."""
    pass

class ContinueSignal(Exception):
    """Salta a la siguiente iteración del ciclo más interno (continue)."""
    pass


# ──────────────────────────────────────────────────────────────
# INTÉRPRETE v4
# ──────────────────────────────────────────────────────────────

class InterpreterVisitor(gramatica_v4Visitor):

    def __init__(self):
        self.tabla     = TablaSimbolos()
        self.funciones = {}   # nombre → FuncDeclContext
        # Registro de structs: nombre_struct → {campo: tipo}
        self._structs: dict[str, dict[str, str]] = {}

    # ──────────────────────────────────────────────────────────
    # PROGRAMA — dos pasadas
    # ──────────────────────────────────────────────────────────

    def visitProgram(self, ctx: gramatica_v4Parser.ProgramContext):
        nombre = ctx.ID().getText() if ctx.ID() else "programa"
        print("=" * 55)
        print(f"  Iniciando ejecución de '{nombre}'")
        print("=" * 55 + "\n")

        # Pasada 1: registrar structs y funciones
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v4Parser.TopStructDeclContext):
                self._registrar_struct(decl.structDecl())
            elif isinstance(decl, gramatica_v4Parser.TopFuncDeclContext):
                nombre_f = decl.funcDecl().ID().getText()
                self.funciones[nombre_f] = decl.funcDecl()

        # Pasada 2: ejecutar sentencias en orden
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v4Parser.TopStatementContext):
                self.visit(decl.statement())

        print("\n" + "=" * 55)
        print("  Fin del programa")
        print("=" * 55)
        self.tabla.imprimir()

    # ──────────────────────────────────────────────────────────
    # STRUCTS (novedad v4)
    # ──────────────────────────────────────────────────────────

    def _registrar_struct(self, ctx: gramatica_v4Parser.StructDeclContext):
        """Registra la definición del struct en el intérprete."""
        nombre = ctx.ID().getText()
        campos = {}
        for campo in ctx.structField():
            tipo_c   = campo.t_type().getText()
            nombre_c = campo.ID().getText()
            campos[nombre_c] = tipo_c
        self._structs[nombre] = campos
        print(f"  [Struct]      '{nombre}' registrado con campos: {list(campos.keys())}")

    def visitTopStructDecl(self, ctx: gramatica_v4Parser.TopStructDeclContext):
        pass   # ya registrado en la pasada 1

    def visitStructVarDecl(self, ctx: gramatica_v4Parser.StructVarDeclContext):
        """Declaración de variable struct: Punto p;"""
        tipo_struct = ctx.ID(0).getText()
        nombre_var  = ctx.ID(1).getText()

        if tipo_struct not in self._structs:
            raise Exception(f"[Error] Struct '{tipo_struct}' no fue declarado.")

        # Inicializar todos los campos con su valor por defecto
        campos = self._structs[tipo_struct]
        defaults = {'int': 0, 'float': 0.0, 'bool': False, 'string': ''}
        valor_inicial = {c: defaults.get(t, None) for c, t in campos.items()}

        self.tabla.declarar_variable(nombre_var, tipo_struct, valor_inicial)
        print(f"  [Struct Var]  {tipo_struct:12} {nombre_var} = {valor_inicial!r}")

    def visitFieldAssign(self, ctx: gramatica_v4Parser.FieldAssignContext):
        """p.x = expr;"""
        nombre_var   = ctx.ID(0).getText()
        nombre_campo = ctx.ID(1).getText()

        simbolo = self.tabla.buscar(nombre_var)
        if simbolo is None:
            raise Exception(f"[Error] Variable '{nombre_var}' no fue declarada.")

        instancia = simbolo['valor']
        tipo_struct = simbolo['tipo']

        if tipo_struct not in self._structs:
            raise Exception(f"[Error] '{nombre_var}' no es un struct.")
        if nombre_campo not in self._structs[tipo_struct]:
            raise Exception(
                f"[Error] El struct '{tipo_struct}' no tiene campo '{nombre_campo}'."
            )

        tipo_campo = self._structs[tipo_struct][nombre_campo]
        valor = self.convertir(self.visit(ctx.expr()), tipo_campo)
        instancia[nombre_campo] = valor
        self.tabla.asignar(nombre_var, instancia)
        print(f"  [Field Asign] {nombre_var}.{nombre_campo} = {valor!r}")
        return valor

    # ──────────────────────────────────────────────────────────
    # IMPORTS — ignorados en tiempo de ejecución
    # ──────────────────────────────────────────────────────────

    def visitTopImport(self, ctx: gramatica_v4Parser.TopImportContext):
        pass

    # ──────────────────────────────────────────────────────────
    # DECLARACIONES DE NIVEL SUPERIOR
    # ──────────────────────────────────────────────────────────

    def visitTopFuncDecl(self, ctx: gramatica_v4Parser.TopFuncDeclContext):
        pass   # ya registradas en la pasada 1

    def visitTopStatement(self, ctx: gramatica_v4Parser.TopStatementContext):
        self.visit(ctx.statement())

    # ──────────────────────────────────────────────────────────
    # SENTENCIAS
    # ──────────────────────────────────────────────────────────

    def visitVarDecl(self, ctx: gramatica_v4Parser.VarDeclContext):
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

    def visitArrayDecl(self, ctx: gramatica_v4Parser.ArrayDeclContext):
        """int[] nums = [1, 2, 3];"""
        texto_tipo = ctx.arrayType().getText()
        if 'int'    in texto_tipo: tipo_base = 'int'
        elif 'float' in texto_tipo: tipo_base = 'float'
        elif 'bool'  in texto_tipo: tipo_base = 'bool'
        else:                       tipo_base = 'string'

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

    def visitAssignment(self, ctx: gramatica_v4Parser.AssignmentContext):
        nombre = ctx.ID().getText()
        tipo   = self.tabla.obtener_tipo(nombre)
        valor  = self.convertir(self.visit(ctx.expr()), tipo)
        self.tabla.asignar(nombre, valor)
        print(f"  [Asignación]  {nombre:12} = {valor!r}")
        return valor

    def visitArrayAssign(self, ctx: gramatica_v4Parser.ArrayAssignContext):
        """nums[i] = expr;"""
        nombre  = ctx.ID().getText()
        simbolo = self.tabla.buscar(nombre)
        if simbolo is None:
            raise Exception(f"[Error] Arreglo '{nombre}' no declarado.")

        arreglo   = simbolo['valor']
        idx       = int(self.visit(ctx.expr(0)))
        tipo_base = simbolo['tipo'].replace('[]', '')
        valor     = self.convertir(self.visit(ctx.expr(1)), tipo_base)

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

    def visitIfStatement(self, ctx: gramatica_v4Parser.IfStatementContext):
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

    def visitWhileStatement(self, ctx: gramatica_v4Parser.WhileStatementContext):
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

    def visitForStatement(self, ctx: gramatica_v4Parser.ForStatementContext):
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

    def visitSwitchStatement(self, ctx: gramatica_v4Parser.SwitchStatementContext):
        """
        switch(expr) { case v1: ...; case v2: ...; default: ...; }
        Implementado con cadena de if/elif en Python.
        Soporta break (BreakSignal) dentro de cada case.
        """
        valor_control = self.visit(ctx.expr())
        print(f"  [SWITCH] valor de control = {valor_control!r}")

        encontrado = False
        try:
            for case_clause in ctx.caseClause():
                valor_case = self.visit(case_clause.expr())
                if not encontrado and valor_control == valor_case:
                    encontrado = True
                    print(f"  [SWITCH] match en case {valor_case!r}")
                # Fall-through: si ya encontramos un case, ejecutar también los siguientes
                if encontrado:
                    self.tabla.push_scope()
                    try:
                        for stmt in case_clause.statement():
                            self.visit(stmt)
                    except BreakSignal:
                        self.tabla.pop_scope()
                        print("  [SWITCH] break — saliendo del switch")
                        return
                    self.tabla.pop_scope()

            # Ejecutar default si ningún case coincidió
            if not encontrado and ctx.defaultClause():
                print("  [SWITCH] ejecutando default")
                self.tabla.push_scope()
                try:
                    for stmt in ctx.defaultClause().statement():
                        self.visit(stmt)
                except BreakSignal:
                    self.tabla.pop_scope()
                    print("  [SWITCH] break — saliendo del switch (default)")
                    return
                self.tabla.pop_scope()

        except BreakSignal:
            print("  [SWITCH] break — saliendo del switch")

    def visitForInitDecl(self, ctx: gramatica_v4Parser.ForInitDeclContext):
        tipo   = ctx.t_type().getText()
        nombre = ctx.ID().getText()
        valor  = self.convertir(self.visit(ctx.expr()), tipo)
        self.tabla.declarar_variable(nombre, tipo, valor)

    def visitForInitAssign(self, ctx: gramatica_v4Parser.ForInitAssignContext):
        nombre = ctx.ID().getText()
        tipo   = self.tabla.obtener_tipo(nombre)
        valor  = self.convertir(self.visit(ctx.expr()), tipo)
        self.tabla.asignar(nombre, valor)

    def visitForUpdate(self, ctx: gramatica_v4Parser.ForUpdateContext):
        nombre = ctx.ID().getText()
        tipo   = self.tabla.obtener_tipo(nombre)
        valor  = self.convertir(self.visit(ctx.expr()), tipo)
        self.tabla.asignar(nombre, valor)

    def visitReturnStatement(self, ctx: gramatica_v4Parser.ReturnStatementContext):
        valor = self.visit(ctx.expr()) if ctx.expr() else None
        raise ReturnSignal(valor)

    def visitBreakStatement(self, ctx: gramatica_v4Parser.BreakStatementContext):
        raise BreakSignal()

    def visitContinueStatement(self, ctx: gramatica_v4Parser.ContinueStatementContext):
        raise ContinueSignal()

    def visitPrintStatement(self, ctx: gramatica_v4Parser.PrintStatementContext):
        valor = self.visit(ctx.expr())
        print(valor)
        return valor

    def visitExprStatement(self, ctx: gramatica_v4Parser.ExprStatementContext):
        return self.visit(ctx.expr())

    def visitBlock(self, ctx: gramatica_v4Parser.BlockContext):
        return self.visitChildren(ctx)

    # ──────────────────────────────────────────────────────────
    # LLAMADA A FUNCIÓN
    # ──────────────────────────────────────────────────────────

    def visitFuncCallExpr(self, ctx: gramatica_v4Parser.FuncCallExprContext):
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
    # EXPRESIONES NUEVAS v4
    # ──────────────────────────────────────────────────────────

    def visitTernaryExpr(self, ctx: gramatica_v4Parser.TernaryExprContext):
        """cond ? expr_verdadero : expr_falso"""
        condicion = bool(self.visit(ctx.expr(0)))
        if condicion:
            return self.visit(ctx.expr(1))
        else:
            return self.visit(ctx.expr(2))

    def visitCastExpr(self, ctx: gramatica_v4Parser.CastExprContext):
        """(tipo) expr  → cast explícito de tipos"""
        tipo_dest = ctx.t_type().getText()
        valor     = self.visit(ctx.expr())
        return self.convertir(valor, tipo_dest)

    def visitFieldAccessExpr(self, ctx: gramatica_v4Parser.FieldAccessExprContext):
        """p.x  → lectura del campo de un struct"""
        nombre_var   = ctx.ID(0).getText()
        nombre_campo = ctx.ID(1).getText()

        simbolo = self.tabla.buscar(nombre_var)
        if simbolo is None:
            raise Exception(f"[Error] Variable '{nombre_var}' no fue declarada.")

        instancia = simbolo['valor']
        if not isinstance(instancia, dict):
            raise Exception(f"[Error] '{nombre_var}' no es un struct.")
        if nombre_campo not in instancia:
            raise Exception(
                f"[Error] El struct no tiene el campo '{nombre_campo}'."
            )
        return instancia[nombre_campo]

    # ──────────────────────────────────────────────────────────
    # EXPRESIONES ARITMÉTICAS Y LÓGICAS
    # ──────────────────────────────────────────────────────────

    def visitMulExpr(self, ctx: gramatica_v4Parser.MulExprContext):
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

    def visitAddExpr(self, ctx: gramatica_v4Parser.AddExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()
        return izq + der if op == '+' else izq - der

    def visitRelExpr(self, ctx: gramatica_v4Parser.RelExprContext):
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

    def visitAndExpr(self, ctx: gramatica_v4Parser.AndExprContext):
        return bool(self.visit(ctx.expr(0))) and bool(self.visit(ctx.expr(1)))

    def visitOrExpr(self, ctx: gramatica_v4Parser.OrExprContext):
        return bool(self.visit(ctx.expr(0))) or bool(self.visit(ctx.expr(1)))

    def visitNotExpr(self, ctx: gramatica_v4Parser.NotExprContext):
        return not bool(self.visit(ctx.expr()))

    def visitNegExpr(self, ctx: gramatica_v4Parser.NegExprContext):
        return -self.visit(ctx.expr())

    def visitParenExpr(self, ctx: gramatica_v4Parser.ParenExprContext):
        return self.visit(ctx.expr())

    # ──────────────────────────────────────────────────────────
    # ACCESO A ARREGLOS
    # ──────────────────────────────────────────────────────────

    def visitArrayAccessExpr(self, ctx: gramatica_v4Parser.ArrayAccessExprContext):
        """nums[i]"""
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

    def visitNumExpr(self, ctx: gramatica_v4Parser.NumExprContext):
        return int(ctx.NUM().getText())

    def visitFloatExpr(self, ctx: gramatica_v4Parser.FloatExprContext):
        return float(ctx.FLOAT_LIT().getText())

    def visitBoolExpr(self, ctx: gramatica_v4Parser.BoolExprContext):
        return ctx.BOOL_LIT().getText() == 'true'

    def visitStringExpr(self, ctx: gramatica_v4Parser.StringExprContext):
        return ctx.STRING_LIT().getText()[1:-1]   # quitar comillas

    def visitIdExpr(self, ctx: gramatica_v4Parser.IdExprContext):
        nombre  = ctx.ID().getText()
        simbolo = self.tabla.buscar(nombre)
        if simbolo is None:
            raise Exception(f"[Error] Variable '{nombre}' no fue declarada.")
        return simbolo['valor']

    # ──────────────────────────────────────────────────────────
    # CONVERSIÓN DE TIPOS
    # ──────────────────────────────────────────────────────────

    def convertir(self, valor, tipo: str):
        """Convierte un valor Python al tipo dado."""
        if tipo.endswith('[]'):
            return valor if isinstance(valor, list) else []
        if tipo == 'int':
            if isinstance(valor, bool): return int(valor)
            return int(valor)   if valor is not None else 0
        if tipo == 'float':
            return float(valor) if valor is not None else 0.0
        if tipo == 'bool':
            return bool(valor)
        if tipo == 'string':
            return str(valor)   if valor is not None else ''
        return valor