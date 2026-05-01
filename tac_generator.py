# ================================================================
# tac_generator.py
# Visitor Generador de Código de Tres Direcciones (TAC)
# Recorre el AST validado y emite instrucciones TAC a un archivo .tac
# ================================================================

from antlr4 import *
from gramatica_v3Parser  import gramatica_v3Parser
from gramatica_v3Visitor import gramatica_v3Visitor


class TACGenerator(gramatica_v3Visitor):

    def __init__(self):
        self.instrucciones: list[str] = []
        self._temp_count  = 0   # contador de temporales: t1, t2, ...
        self._label_count = 0   # contador de etiquetas:  L1, L2, ...

    # ──────────────────────────────────────────────────────────
    # UTILIDADES INTERNAS
    # ──────────────────────────────────────────────────────────

    def _nuevo_temp(self) -> str:
        """Genera un nuevo nombre de temporal: t1, t2, ..."""
        self._temp_count += 1
        return f"t{self._temp_count}"

    def _nueva_etiqueta(self) -> str:
        """Genera una nueva etiqueta de salto: L1, L2, ..."""
        self._label_count += 1
        return f"L{self._label_count}"

    def _emit(self, instruccion: str):
        """Agrega una línea de TAC a la lista."""
        self.instrucciones.append(instruccion)

    def _emit_label(self, etiqueta: str):
        """Agrega una etiqueta al TAC (sin indentación)."""
        self.instrucciones.append(f"{etiqueta}:")

    def guardar(self, ruta: str):
        """Escribe todas las instrucciones en un archivo .tac"""
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.instrucciones))
            f.write('\n')

    def obtener_texto(self) -> str:
        """Retorna el TAC completo como string (para la UI)."""
        return '\n'.join(self.instrucciones)

    # ──────────────────────────────────────────────────────────
    # PROGRAMA
    # ──────────────────────────────────────────────────────────

    def visitProgram(self, ctx: gramatica_v3Parser.ProgramContext):
        nombre = ctx.ID().getText() if ctx.ID() else "programa"
        self._emit(f"# === Programa: {nombre} ===")
        self._emit("")

        # Pasada 1: emitir funciones primero
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v3Parser.TopFuncDeclContext):
                self.visit(decl)

        # Pasada 2: emitir código principal
        self._emit("# --- Código principal ---")
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v3Parser.TopStatementContext):
                self.visit(decl.statement())

    def visitTopImport(self, ctx: gramatica_v3Parser.TopImportContext):
        modulo = ctx.importDecl().ID().getText()
        self._emit(f"# import {modulo}")

    # ──────────────────────────────────────────────────────────
    # FUNCIONES
    # ──────────────────────────────────────────────────────────

    def visitTopFuncDecl(self, ctx: gramatica_v3Parser.TopFuncDeclContext):
        self.visit(ctx.funcDecl())

    def visitFuncDecl(self, ctx: gramatica_v3Parser.FuncDeclContext):
        nombre = ctx.ID().getText()
        self._emit("")
        self._emit(f"begin_func {nombre}")

        # Emitir parámetros
        if ctx.paramList():
            for p in ctx.paramList().param():
                nombre_param = p.ID().getText()
                self._emit(f"    param {nombre_param}")

        # Emitir cuerpo
        self.visit(ctx.block())
        self._emit(f"end_func {nombre}")
        self._emit("")

    # ──────────────────────────────────────────────────────────
    # SENTENCIAS
    # ──────────────────────────────────────────────────────────

    def visitVarDecl(self, ctx: gramatica_v3Parser.VarDeclContext):
        nombre = ctx.ID().getText()
        if ctx.expr():
            temp = self.visit(ctx.expr())
            self._emit(f"    {nombre} = {temp}")
        else:
            # Valor por defecto según tipo
            tipo = ctx.t_type().getText()
            defaults = {'int': '0', 'float': '0.0', 'bool': 'false', 'string': '""'}
            self._emit(f"    {nombre} = {defaults.get(tipo, '0')}")

    def visitArrayDecl(self, ctx: gramatica_v3Parser.ArrayDeclContext):
        nombre = ctx.ID().getText()
        if ctx.arrayLiteral():
            elementos = []
            for expr in ctx.arrayLiteral().expr():
                temp = self.visit(expr)
                elementos.append(str(temp))
            self._emit(f"    {nombre} = [{', '.join(elementos)}]")
        else:
            self._emit(f"    {nombre} = []")

    def visitAssignment(self, ctx: gramatica_v3Parser.AssignmentContext):
        nombre = ctx.ID().getText()
        temp   = self.visit(ctx.expr())
        self._emit(f"    {nombre} = {temp}")

    def visitArrayAssign(self, ctx: gramatica_v3Parser.ArrayAssignContext):
        nombre  = ctx.ID().getText()
        idx     = self.visit(ctx.expr(0))
        valor   = self.visit(ctx.expr(1))
        self._emit(f"    {nombre}[{idx}] = {valor}")

    def visitIfStatement(self, ctx: gramatica_v3Parser.IfStatementContext):
        cond    = self.visit(ctx.expr())
        L_true  = self._nueva_etiqueta()
        L_false = self._nueva_etiqueta()
        L_fin   = self._nueva_etiqueta()

        if ctx.ELSE():
            # if cond goto L_true
            self._emit(f"    if {cond} goto {L_true}")
            self._emit(f"    goto {L_false}")
            self._emit_label(L_true)
            self.visit(ctx.block(0))
            self._emit(f"    goto {L_fin}")
            self._emit_label(L_false)
            self.visit(ctx.block(1))
            self._emit_label(L_fin)
        else:
            self._emit(f"    if {cond} goto {L_true}")
            self._emit(f"    goto {L_fin}")
            self._emit_label(L_true)
            self.visit(ctx.block(0))
            self._emit_label(L_fin)

    def visitWhileStatement(self, ctx: gramatica_v3Parser.WhileStatementContext):
        L_inicio  = self._nueva_etiqueta()
        L_cuerpo  = self._nueva_etiqueta()
        L_fin     = self._nueva_etiqueta()

        # Guardar etiquetas para break/continue
        self._push_loop(L_inicio, L_fin)

        self._emit_label(L_inicio)
        cond = self.visit(ctx.expr())
        self._emit(f"    if {cond} goto {L_cuerpo}")
        self._emit(f"    goto {L_fin}")
        self._emit_label(L_cuerpo)
        self.visit(ctx.block())
        self._emit(f"    goto {L_inicio}")
        self._emit_label(L_fin)

        self._pop_loop()

    def visitForStatement(self, ctx: gramatica_v3Parser.ForStatementContext):
        L_inicio = self._nueva_etiqueta()
        L_cuerpo = self._nueva_etiqueta()
        L_fin    = self._nueva_etiqueta()
        L_update = self._nueva_etiqueta()

        self._push_loop(L_update, L_fin)

        # Inicialización
        self.visit(ctx.forInit())
        self._emit_label(L_inicio)

        # Condición
        cond = self.visit(ctx.expr())
        self._emit(f"    if {cond} goto {L_cuerpo}")
        self._emit(f"    goto {L_fin}")
        self._emit_label(L_cuerpo)

        # Cuerpo
        self.visit(ctx.block())

        # Actualización
        self._emit_label(L_update)
        self.visit(ctx.forUpdate())
        self._emit(f"    goto {L_inicio}")
        self._emit_label(L_fin)

        self._pop_loop()

    def visitForInitDecl(self, ctx: gramatica_v3Parser.ForInitDeclContext):
        nombre = ctx.ID().getText()
        temp   = self.visit(ctx.expr())
        self._emit(f"    {nombre} = {temp}")

    def visitForInitAssign(self, ctx: gramatica_v3Parser.ForInitAssignContext):
        nombre = ctx.ID().getText()
        temp   = self.visit(ctx.expr())
        self._emit(f"    {nombre} = {temp}")

    def visitForUpdate(self, ctx: gramatica_v3Parser.ForUpdateContext):
        nombre = ctx.ID().getText()
        temp   = self.visit(ctx.expr())
        self._emit(f"    {nombre} = {temp}")

    def visitReturnStatement(self, ctx: gramatica_v3Parser.ReturnStatementContext):
        if ctx.expr():
            temp = self.visit(ctx.expr())
            self._emit(f"    return {temp}")
        else:
            self._emit("    return")

    def visitBreakStatement(self, ctx: gramatica_v3Parser.BreakStatementContext):
        etiqueta_fin = self._loop_fin_actual()
        self._emit(f"    goto {etiqueta_fin}    # break")

    def visitContinueStatement(self, ctx: gramatica_v3Parser.ContinueStatementContext):
        etiqueta_inicio = self._loop_inicio_actual()
        self._emit(f"    goto {etiqueta_inicio}    # continue")

    def visitPrintStatement(self, ctx: gramatica_v3Parser.PrintStatementContext):
        temp = self.visit(ctx.expr())
        self._emit(f"    print {temp}")

    def visitExprStatement(self, ctx: gramatica_v3Parser.ExprStatementContext):
        self.visit(ctx.expr())

    def visitBlock(self, ctx: gramatica_v3Parser.BlockContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    # ──────────────────────────────────────────────────────────
    # EXPRESIONES — retornan el nombre del temporal o literal
    # ──────────────────────────────────────────────────────────

    def visitMulExpr(self, ctx: gramatica_v3Parser.MulExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()
        t   = self._nuevo_temp()
        self._emit(f"    {t} = {izq} {op} {der}")
        return t

    def visitAddExpr(self, ctx: gramatica_v3Parser.AddExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()
        t   = self._nuevo_temp()
        self._emit(f"    {t} = {izq} {op} {der}")
        return t

    def visitRelExpr(self, ctx: gramatica_v3Parser.RelExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()
        t   = self._nuevo_temp()
        self._emit(f"    {t} = {izq} {op} {der}")
        return t

    def visitAndExpr(self, ctx: gramatica_v3Parser.AndExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        t   = self._nuevo_temp()
        self._emit(f"    {t} = {izq} && {der}")
        return t

    def visitOrExpr(self, ctx: gramatica_v3Parser.OrExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        t   = self._nuevo_temp()
        self._emit(f"    {t} = {izq} || {der}")
        return t

    def visitNotExpr(self, ctx: gramatica_v3Parser.NotExprContext):
        operando = self.visit(ctx.expr())
        t        = self._nuevo_temp()
        self._emit(f"    {t} = !{operando}")
        return t

    def visitNegExpr(self, ctx: gramatica_v3Parser.NegExprContext):
        operando = self.visit(ctx.expr())
        t        = self._nuevo_temp()
        self._emit(f"    {t} = -{operando}")
        return t

    def visitArrayAccessExpr(self, ctx: gramatica_v3Parser.ArrayAccessExprContext):
        nombre = ctx.ID().getText()
        idx    = self.visit(ctx.expr())
        t      = self._nuevo_temp()
        self._emit(f"    {t} = {nombre}[{idx}]")
        return t

    def visitFuncCallExpr(self, ctx: gramatica_v3Parser.FuncCallExprContext):
        nombre = ctx.ID().getText()
        args   = []
        if ctx.argList():
            for arg in ctx.argList().expr():
                args.append(self.visit(arg))

        # Emitir parámetros en orden inverso (convención TAC)
        for arg in args:
            self._emit(f"    push {arg}")

        t = self._nuevo_temp()
        self._emit(f"    {t} = call {nombre}, {len(args)}")
        return t

    def visitParenExpr(self, ctx: gramatica_v3Parser.ParenExprContext):
        return self.visit(ctx.expr())

    # ──────────────────────────────────────────────────────────
    # LITERALES — retornan el valor como string
    # ──────────────────────────────────────────────────────────

    def visitNumExpr(self, ctx: gramatica_v3Parser.NumExprContext):
        return ctx.NUM().getText()

    def visitFloatExpr(self, ctx: gramatica_v3Parser.FloatExprContext):
        return ctx.FLOAT_LIT().getText()

    def visitBoolExpr(self, ctx: gramatica_v3Parser.BoolExprContext):
        return ctx.BOOL_LIT().getText()

    def visitStringExpr(self, ctx: gramatica_v3Parser.StringExprContext):
        return ctx.STRING_LIT().getText()

    def visitIdExpr(self, ctx: gramatica_v3Parser.IdExprContext):
        return ctx.ID().getText()

    # ──────────────────────────────────────────────────────────
    # SOPORTE PARA BREAK / CONTINUE (pila de ciclos)
    # ──────────────────────────────────────────────────────────

    # Pila: cada entrada es (etiqueta_continue, etiqueta_break)
    _pila_ciclos: list = []

    def _push_loop(self, etiqueta_inicio: str, etiqueta_fin: str):
        self._pila_ciclos.append((etiqueta_inicio, etiqueta_fin))

    def _pop_loop(self):
        if self._pila_ciclos:
            self._pila_ciclos.pop()

    def _loop_inicio_actual(self) -> str:
        """Etiqueta de continue: vuelve al inicio del ciclo más interno."""
        return self._pila_ciclos[-1][0] if self._pila_ciclos else "L_ERR"

    def _loop_fin_actual(self) -> str:
        """Etiqueta de break: sale del ciclo más interno."""
        return self._pila_ciclos[-1][1] if self._pila_ciclos else "L_ERR"
