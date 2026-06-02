# ================================================================
# tac_generator_v4.py
# Visitor Generador de Código de Tres Direcciones (TAC) — v4
# Novedades: switch/case, operador ternario, cast explícito, structs
# ================================================================

from antlr4 import *
from gramatica_v4Parser  import gramatica_v4Parser
from gramatica_v4Visitor import gramatica_v4Visitor


class TACGenerator(gramatica_v4Visitor):

    def __init__(self):
        self.instrucciones: list[str] = []
        self._temp_count  = 0
        self._label_count = 0
        # Pila de ciclos: (etiqueta_continue, etiqueta_break)
        self._pila_ciclos:  list[tuple[str, str]] = []
        # Pila de switch: etiqueta_fin para break
        self._pila_switch:  list[str] = []
        # Registro de structs: nombre → {campo: índice}
        self._structs: dict[str, dict[str, int]] = {}

    # ──────────────────────────────────────────────────────────
    # UTILIDADES
    # ──────────────────────────────────────────────────────────

    def _nuevo_temp(self) -> str:
        self._temp_count += 1
        return f"t{self._temp_count}"

    def _nueva_etiqueta(self) -> str:
        self._label_count += 1
        return f"L{self._label_count}"

    def _emit(self, instruccion: str):
        self.instrucciones.append(instruccion)

    def _emit_label(self, etiqueta: str):
        self.instrucciones.append(f"{etiqueta}:")

    def guardar(self, ruta: str):
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.instrucciones) + '\n')

    def obtener_texto(self) -> str:
        return '\n'.join(self.instrucciones)

    # ──────────────────────────────────────────────────────────
    # PILA DE CONTROL (break / continue)
    # ──────────────────────────────────────────────────────────

    def _push_loop(self, lbl_continue: str, lbl_break: str):
        self._pila_ciclos.append((lbl_continue, lbl_break))

    def _pop_loop(self):
        if self._pila_ciclos:
            self._pila_ciclos.pop()

    def _loop_continue(self) -> str:
        return self._pila_ciclos[-1][0] if self._pila_ciclos else "L_ERR"

    def _loop_break(self) -> str:
        return self._pila_ciclos[-1][1] if self._pila_ciclos else "L_ERR"

    def _push_switch(self, lbl_fin: str):
        self._pila_switch.append(lbl_fin)

    def _pop_switch(self):
        if self._pila_switch:
            self._pila_switch.pop()

    def _switch_break(self) -> str:
        return self._pila_switch[-1] if self._pila_switch else "L_ERR"

    # ──────────────────────────────────────────────────────────
    # PROGRAMA
    # ──────────────────────────────────────────────────────────

    def visitProgram(self, ctx: gramatica_v4Parser.ProgramContext):
        nombre = ctx.ID().getText() if ctx.ID() else "programa"
        self._emit(f"# === Programa: {nombre} ===")
        self._emit("")

        # Pasada 1: structs y funciones
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v4Parser.TopStructDeclContext):
                self.visit(decl)
            elif isinstance(decl, gramatica_v4Parser.TopFuncDeclContext):
                self.visit(decl)

        # Pasada 2: código principal
        self._emit("# --- Código principal ---")
        for decl in ctx.topLevelDecl():
            if isinstance(decl, gramatica_v4Parser.TopStatementContext):
                self.visit(decl.statement())

    def visitTopImport(self, ctx: gramatica_v4Parser.TopImportContext):
        self._emit(f"# import {ctx.importDecl().ID().getText()}")

    # ──────────────────────────────────────────────────────────
    # STRUCTS (novedad v4)
    # ──────────────────────────────────────────────────────────

    def visitTopStructDecl(self, ctx: gramatica_v4Parser.TopStructDeclContext):
        self.visit(ctx.structDecl())

    def visitStructDecl(self, ctx: gramatica_v4Parser.StructDeclContext):
        """Registra la definición del struct y emite su cabecera TAC."""
        nombre = ctx.ID().getText()
        campos = {}
        self._emit("")
        self._emit(f"# struct {nombre}:")
        for i, campo in enumerate(ctx.structField()):
            tipo_c   = campo.t_type().getText()
            nombre_c = campo.ID().getText()
            campos[nombre_c] = i
            self._emit(f"#   campo[{i}]: {tipo_c} {nombre_c}")
        self._structs[nombre] = campos
        self._emit("")

    def visitStructVarDecl(self, ctx: gramatica_v4Parser.StructVarDeclContext):
        """Declaración: Punto p;"""
        tipo_struct = ctx.ID(0).getText()
        nombre_var  = ctx.ID(1).getText()
        self._emit(f"    alloc {tipo_struct} {nombre_var}")

    # ──────────────────────────────────────────────────────────
    # FUNCIONES
    # ──────────────────────────────────────────────────────────

    def visitTopFuncDecl(self, ctx: gramatica_v4Parser.TopFuncDeclContext):
        self.visit(ctx.funcDecl())

    def visitFuncDecl(self, ctx: gramatica_v4Parser.FuncDeclContext):
        nombre = ctx.ID().getText()
        self._emit("")
        self._emit(f"begin_func {nombre}")
        if ctx.paramList():
            for p in ctx.paramList().param():
                self._emit(f"    param {p.ID().getText()}")
        self.visit(ctx.block())
        self._emit(f"end_func {nombre}")
        self._emit("")

    # ──────────────────────────────────────────────────────────
    # SENTENCIAS
    # ──────────────────────────────────────────────────────────

    def visitVarDecl(self, ctx: gramatica_v4Parser.VarDeclContext):
        nombre = ctx.ID().getText()
        if ctx.expr():
            temp = self.visit(ctx.expr())
            self._emit(f"    {nombre} = {temp}")
        else:
            tipo = ctx.t_type().getText()
            defaults = {'int': '0', 'float': '0.0', 'bool': 'false', 'string': '""'}
            self._emit(f"    {nombre} = {defaults.get(tipo, '0')}")

    def visitArrayDecl(self, ctx: gramatica_v4Parser.ArrayDeclContext):
        nombre = ctx.ID().getText()
        if ctx.arrayLiteral():
            elems = [str(self.visit(e)) for e in ctx.arrayLiteral().expr()]
            self._emit(f"    {nombre} = [{', '.join(elems)}]")
        else:
            self._emit(f"    {nombre} = []")

    def visitAssignment(self, ctx: gramatica_v4Parser.AssignmentContext):
        nombre = ctx.ID().getText()
        temp   = self.visit(ctx.expr())
        self._emit(f"    {nombre} = {temp}")

    def visitFieldAssign(self, ctx: gramatica_v4Parser.FieldAssignContext):
        """p.x = expr  →  TAC: p.x = t1"""
        var   = ctx.ID(0).getText()
        campo = ctx.ID(1).getText()
        temp  = self.visit(ctx.expr())
        self._emit(f"    {var}.{campo} = {temp}")

    def visitArrayAssign(self, ctx: gramatica_v4Parser.ArrayAssignContext):
        nombre = ctx.ID().getText()
        idx    = self.visit(ctx.expr(0))
        valor  = self.visit(ctx.expr(1))
        self._emit(f"    {nombre}[{idx}] = {valor}")

    def visitIfStatement(self, ctx: gramatica_v4Parser.IfStatementContext):
        cond   = self.visit(ctx.expr())
        L_true = self._nueva_etiqueta()
        L_fin  = self._nueva_etiqueta()

        if ctx.ELSE():
            L_false = self._nueva_etiqueta()
            self._emit(f"    if {cond} goto {L_true}")
            self._emit(f"    goto {L_false}")
            self._emit_label(L_true)
            self.visit(ctx.block(0))
            self._emit(f"    goto {L_fin}")
            self._emit_label(L_false)
            self.visit(ctx.block(1))
        else:
            self._emit(f"    if {cond} goto {L_true}")
            self._emit(f"    goto {L_fin}")
            self._emit_label(L_true)
            self.visit(ctx.block(0))

        self._emit_label(L_fin)

    def visitWhileStatement(self, ctx: gramatica_v4Parser.WhileStatementContext):
        L_inicio = self._nueva_etiqueta()
        L_cuerpo = self._nueva_etiqueta()
        L_fin    = self._nueva_etiqueta()

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

    def visitForStatement(self, ctx: gramatica_v4Parser.ForStatementContext):
        L_inicio = self._nueva_etiqueta()
        L_cuerpo = self._nueva_etiqueta()
        L_update = self._nueva_etiqueta()
        L_fin    = self._nueva_etiqueta()

        self._push_loop(L_update, L_fin)
        self.visit(ctx.forInit())
        self._emit_label(L_inicio)
        cond = self.visit(ctx.expr())
        self._emit(f"    if {cond} goto {L_cuerpo}")
        self._emit(f"    goto {L_fin}")
        self._emit_label(L_cuerpo)
        self.visit(ctx.block())
        self._emit_label(L_update)
        self.visit(ctx.forUpdate())
        self._emit(f"    goto {L_inicio}")
        self._emit_label(L_fin)
        self._pop_loop()

    def visitSwitchStatement(self, ctx: gramatica_v4Parser.SwitchStatementContext):
        """
        switch(x) { case 1: ...; break; default: ...; }
        TAC: saltos condicionales encadenados sobre el valor de control.
        """
        L_fin     = self._nueva_etiqueta()
        L_default = self._nueva_etiqueta()

        self._push_switch(L_fin)

        # Evaluar expresión de control una sola vez
        t_ctrl = self.visit(ctx.expr())
        self._emit(f"    # switch sobre {t_ctrl}")

        # Generar etiquetas para cada case
        etiquetas_case = []
        for _ in ctx.caseClause():
            etiquetas_case.append(self._nueva_etiqueta())

        # Emitir la cadena de saltos condicionales
        for i, case_clause in enumerate(ctx.caseClause()):
            t_val = self.visit(case_clause.expr())
            t_cmp = self._nuevo_temp()
            self._emit(f"    {t_cmp} = {t_ctrl} == {t_val}")
            self._emit(f"    if {t_cmp} goto {etiquetas_case[i]}")

        # Si ningún case coincide, ir al default (o al fin)
        if ctx.defaultClause():
            self._emit(f"    goto {L_default}")
        else:
            self._emit(f"    goto {L_fin}")

        # Emitir el cuerpo de cada case
        for i, case_clause in enumerate(ctx.caseClause()):
            self._emit_label(etiquetas_case[i])
            for stmt in case_clause.statement():
                self.visit(stmt)
            # Fall-through implícito si no hay break
            # (el break emitirá goto L_fin por sí solo)

        # Emitir el bloque default
        if ctx.defaultClause():
            self._emit_label(L_default)
            for stmt in ctx.defaultClause().statement():
                self.visit(stmt)

        self._emit_label(L_fin)
        self._pop_switch()

    def visitForInitDecl(self, ctx: gramatica_v4Parser.ForInitDeclContext):
        nombre = ctx.ID().getText()
        temp   = self.visit(ctx.expr())
        self._emit(f"    {nombre} = {temp}")

    def visitForInitAssign(self, ctx: gramatica_v4Parser.ForInitAssignContext):
        nombre = ctx.ID().getText()
        temp   = self.visit(ctx.expr())
        self._emit(f"    {nombre} = {temp}")

    def visitForUpdate(self, ctx: gramatica_v4Parser.ForUpdateContext):
        nombre = ctx.ID().getText()
        temp   = self.visit(ctx.expr())
        self._emit(f"    {nombre} = {temp}")

    def visitReturnStatement(self, ctx: gramatica_v4Parser.ReturnStatementContext):
        if ctx.expr():
            temp = self.visit(ctx.expr())
            self._emit(f"    return {temp}")
        else:
            self._emit("    return")

    def visitBreakStatement(self, ctx: gramatica_v4Parser.BreakStatementContext):
        # Si hay switch activo y es más "reciente" que el ciclo, saltar al fin del switch
        if self._pila_switch:
            self._emit(f"    goto {self._switch_break()}    # break (switch)")
        elif self._pila_ciclos:
            self._emit(f"    goto {self._loop_break()}      # break (ciclo)")
        else:
            self._emit("    # ERROR: break fuera de contexto")

    def visitContinueStatement(self, ctx: gramatica_v4Parser.ContinueStatementContext):
        self._emit(f"    goto {self._loop_continue()}    # continue")

    def visitPrintStatement(self, ctx: gramatica_v4Parser.PrintStatementContext):
        temp = self.visit(ctx.expr())
        self._emit(f"    print {temp}")

    def visitExprStatement(self, ctx: gramatica_v4Parser.ExprStatementContext):
        self.visit(ctx.expr())

    def visitBlock(self, ctx: gramatica_v4Parser.BlockContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    # ──────────────────────────────────────────────────────────
    # EXPRESIONES
    # ──────────────────────────────────────────────────────────

    def visitTernaryExpr(self, ctx: gramatica_v4Parser.TernaryExprContext):
        """
        cond ? expr_v : expr_f
        TAC:
            t_cond = evaluate(cond)
            if t_cond goto L_true
            t_result = evaluate(expr_f)
            goto L_fin
        L_true:
            t_result = evaluate(expr_v)
        L_fin:
        """
        t_result = self._nuevo_temp()
        L_true   = self._nueva_etiqueta()
        L_fin    = self._nueva_etiqueta()

        t_cond = self.visit(ctx.expr(0))
        self._emit(f"    if {t_cond} goto {L_true}")

        # Rama falsa
        t_falso = self.visit(ctx.expr(2))
        self._emit(f"    {t_result} = {t_falso}")
        self._emit(f"    goto {L_fin}")

        # Rama verdadera
        self._emit_label(L_true)
        t_verd = self.visit(ctx.expr(1))
        self._emit(f"    {t_result} = {t_verd}")

        self._emit_label(L_fin)
        return t_result

    def visitCastExpr(self, ctx: gramatica_v4Parser.CastExprContext):
        """
        (float) miVar  →  TAC: t1 = cast float miVar
        """
        tipo_dest = ctx.t_type().getText()
        t_origen  = self.visit(ctx.expr())
        t_result  = self._nuevo_temp()
        self._emit(f"    {t_result} = cast {tipo_dest} {t_origen}")
        return t_result

    def visitMulExpr(self, ctx: gramatica_v4Parser.MulExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()
        t   = self._nuevo_temp()
        self._emit(f"    {t} = {izq} {op} {der}")
        return t

    def visitAddExpr(self, ctx: gramatica_v4Parser.AddExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()
        t   = self._nuevo_temp()
        self._emit(f"    {t} = {izq} {op} {der}")
        return t

    def visitRelExpr(self, ctx: gramatica_v4Parser.RelExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op  = ctx.getChild(1).getText()
        t   = self._nuevo_temp()
        self._emit(f"    {t} = {izq} {op} {der}")
        return t

    def visitAndExpr(self, ctx: gramatica_v4Parser.AndExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        t   = self._nuevo_temp()
        self._emit(f"    {t} = {izq} && {der}")
        return t

    def visitOrExpr(self, ctx: gramatica_v4Parser.OrExprContext):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        t   = self._nuevo_temp()
        self._emit(f"    {t} = {izq} || {der}")
        return t

    def visitNotExpr(self, ctx: gramatica_v4Parser.NotExprContext):
        op = self.visit(ctx.expr())
        t  = self._nuevo_temp()
        self._emit(f"    {t} = !{op}")
        return t

    def visitNegExpr(self, ctx: gramatica_v4Parser.NegExprContext):
        op = self.visit(ctx.expr())
        t  = self._nuevo_temp()
        self._emit(f"    {t} = -{op}")
        return t

    def visitArrayAccessExpr(self, ctx: gramatica_v4Parser.ArrayAccessExprContext):
        nombre = ctx.ID().getText()
        idx    = self.visit(ctx.expr())
        t      = self._nuevo_temp()
        self._emit(f"    {t} = {nombre}[{idx}]")
        return t

    def visitFieldAccessExpr(self, ctx: gramatica_v4Parser.FieldAccessExprContext):
        """p.x  →  TAC: t1 = p.x"""
        var   = ctx.ID(0).getText()
        campo = ctx.ID(1).getText()
        t     = self._nuevo_temp()
        self._emit(f"    {t} = {var}.{campo}")
        return t

    def visitFuncCallExpr(self, ctx: gramatica_v4Parser.FuncCallExprContext):
        nombre = ctx.ID().getText()
        args   = []
        if ctx.argList():
            for arg in ctx.argList().expr():
                args.append(self.visit(arg))
        for arg in args:
            self._emit(f"    push {arg}")
        t = self._nuevo_temp()
        self._emit(f"    {t} = call {nombre}, {len(args)}")
        return t

    def visitParenExpr(self, ctx: gramatica_v4Parser.ParenExprContext):
        return self.visit(ctx.expr())

    # ── Literales ──
    def visitNumExpr(self, ctx):    return ctx.NUM().getText()
    def visitFloatExpr(self, ctx):  return ctx.FLOAT_LIT().getText()
    def visitBoolExpr(self, ctx):   return ctx.BOOL_LIT().getText()
    def visitStringExpr(self, ctx): return ctx.STRING_LIT().getText()
    def visitIdExpr(self, ctx):     return ctx.ID().getText()