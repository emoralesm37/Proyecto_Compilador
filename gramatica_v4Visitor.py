# Generated from gramatica_v4.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramatica_v4Parser import gramatica_v4Parser
else:
    from gramatica_v4Parser import gramatica_v4Parser

# This class defines a complete generic visitor for a parse tree produced by gramatica_v4Parser.

class gramatica_v4Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramatica_v4Parser#program.
    def visitProgram(self, ctx:gramatica_v4Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#topFuncDecl.
    def visitTopFuncDecl(self, ctx:gramatica_v4Parser.TopFuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#topImport.
    def visitTopImport(self, ctx:gramatica_v4Parser.TopImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#topStructDecl.
    def visitTopStructDecl(self, ctx:gramatica_v4Parser.TopStructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#topStatement.
    def visitTopStatement(self, ctx:gramatica_v4Parser.TopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#importDecl.
    def visitImportDecl(self, ctx:gramatica_v4Parser.ImportDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#structDecl.
    def visitStructDecl(self, ctx:gramatica_v4Parser.StructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#structField.
    def visitStructField(self, ctx:gramatica_v4Parser.StructFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#funcDecl.
    def visitFuncDecl(self, ctx:gramatica_v4Parser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#returnType.
    def visitReturnType(self, ctx:gramatica_v4Parser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#paramList.
    def visitParamList(self, ctx:gramatica_v4Parser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#param.
    def visitParam(self, ctx:gramatica_v4Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#t_type.
    def visitT_type(self, ctx:gramatica_v4Parser.T_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#intArrayType.
    def visitIntArrayType(self, ctx:gramatica_v4Parser.IntArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#floatArrayType.
    def visitFloatArrayType(self, ctx:gramatica_v4Parser.FloatArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#boolArrayType.
    def visitBoolArrayType(self, ctx:gramatica_v4Parser.BoolArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#stringArrayType.
    def visitStringArrayType(self, ctx:gramatica_v4Parser.StringArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#statement.
    def visitStatement(self, ctx:gramatica_v4Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#varDecl.
    def visitVarDecl(self, ctx:gramatica_v4Parser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#arrayDecl.
    def visitArrayDecl(self, ctx:gramatica_v4Parser.ArrayDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#structVarDecl.
    def visitStructVarDecl(self, ctx:gramatica_v4Parser.StructVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#arrayLiteral.
    def visitArrayLiteral(self, ctx:gramatica_v4Parser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#assignment.
    def visitAssignment(self, ctx:gramatica_v4Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#fieldAssign.
    def visitFieldAssign(self, ctx:gramatica_v4Parser.FieldAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#arrayAssign.
    def visitArrayAssign(self, ctx:gramatica_v4Parser.ArrayAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ifStatement.
    def visitIfStatement(self, ctx:gramatica_v4Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#whileStatement.
    def visitWhileStatement(self, ctx:gramatica_v4Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#forStatement.
    def visitForStatement(self, ctx:gramatica_v4Parser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#switchStatement.
    def visitSwitchStatement(self, ctx:gramatica_v4Parser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#caseClause.
    def visitCaseClause(self, ctx:gramatica_v4Parser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#defaultClause.
    def visitDefaultClause(self, ctx:gramatica_v4Parser.DefaultClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#forInitDecl.
    def visitForInitDecl(self, ctx:gramatica_v4Parser.ForInitDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#forInitAssign.
    def visitForInitAssign(self, ctx:gramatica_v4Parser.ForInitAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#forUpdate.
    def visitForUpdate(self, ctx:gramatica_v4Parser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#returnStatement.
    def visitReturnStatement(self, ctx:gramatica_v4Parser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#breakStatement.
    def visitBreakStatement(self, ctx:gramatica_v4Parser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#continueStatement.
    def visitContinueStatement(self, ctx:gramatica_v4Parser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#printStatement.
    def visitPrintStatement(self, ctx:gramatica_v4Parser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#exprStatement.
    def visitExprStatement(self, ctx:gramatica_v4Parser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#block.
    def visitBlock(self, ctx:gramatica_v4Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#castExpr.
    def visitCastExpr(self, ctx:gramatica_v4Parser.CastExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#fieldAccessExpr.
    def visitFieldAccessExpr(self, ctx:gramatica_v4Parser.FieldAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#orExpr.
    def visitOrExpr(self, ctx:gramatica_v4Parser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#funcCallExpr.
    def visitFuncCallExpr(self, ctx:gramatica_v4Parser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#parenExpr.
    def visitParenExpr(self, ctx:gramatica_v4Parser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#numExpr.
    def visitNumExpr(self, ctx:gramatica_v4Parser.NumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#stringExpr.
    def visitStringExpr(self, ctx:gramatica_v4Parser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#floatExpr.
    def visitFloatExpr(self, ctx:gramatica_v4Parser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#notExpr.
    def visitNotExpr(self, ctx:gramatica_v4Parser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#arrayAccessExpr.
    def visitArrayAccessExpr(self, ctx:gramatica_v4Parser.ArrayAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ternaryExpr.
    def visitTernaryExpr(self, ctx:gramatica_v4Parser.TernaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#addExpr.
    def visitAddExpr(self, ctx:gramatica_v4Parser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#negExpr.
    def visitNegExpr(self, ctx:gramatica_v4Parser.NegExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#mulExpr.
    def visitMulExpr(self, ctx:gramatica_v4Parser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#boolExpr.
    def visitBoolExpr(self, ctx:gramatica_v4Parser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#relExpr.
    def visitRelExpr(self, ctx:gramatica_v4Parser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#idExpr.
    def visitIdExpr(self, ctx:gramatica_v4Parser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#andExpr.
    def visitAndExpr(self, ctx:gramatica_v4Parser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#argList.
    def visitArgList(self, ctx:gramatica_v4Parser.ArgListContext):
        return self.visitChildren(ctx)



del gramatica_v4Parser