# Generated from gramatica_v3.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramatica_v3Parser import gramatica_v3Parser
else:
    from gramatica_v3Parser import gramatica_v3Parser

# This class defines a complete generic visitor for a parse tree produced by gramatica_v3Parser.

class gramatica_v3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramatica_v3Parser#program.
    def visitProgram(self, ctx:gramatica_v3Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#topFuncDecl.
    def visitTopFuncDecl(self, ctx:gramatica_v3Parser.TopFuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#topImport.
    def visitTopImport(self, ctx:gramatica_v3Parser.TopImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#topStatement.
    def visitTopStatement(self, ctx:gramatica_v3Parser.TopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#importDecl.
    def visitImportDecl(self, ctx:gramatica_v3Parser.ImportDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#funcDecl.
    def visitFuncDecl(self, ctx:gramatica_v3Parser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#returnType.
    def visitReturnType(self, ctx:gramatica_v3Parser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#paramList.
    def visitParamList(self, ctx:gramatica_v3Parser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#param.
    def visitParam(self, ctx:gramatica_v3Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#t_type.
    def visitT_type(self, ctx:gramatica_v3Parser.T_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#intArrayType.
    def visitIntArrayType(self, ctx:gramatica_v3Parser.IntArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#floatArrayType.
    def visitFloatArrayType(self, ctx:gramatica_v3Parser.FloatArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#boolArrayType.
    def visitBoolArrayType(self, ctx:gramatica_v3Parser.BoolArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#stringArrayType.
    def visitStringArrayType(self, ctx:gramatica_v3Parser.StringArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#statement.
    def visitStatement(self, ctx:gramatica_v3Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#varDecl.
    def visitVarDecl(self, ctx:gramatica_v3Parser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#arrayDecl.
    def visitArrayDecl(self, ctx:gramatica_v3Parser.ArrayDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#arrayLiteral.
    def visitArrayLiteral(self, ctx:gramatica_v3Parser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#assignment.
    def visitAssignment(self, ctx:gramatica_v3Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#arrayAssign.
    def visitArrayAssign(self, ctx:gramatica_v3Parser.ArrayAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#ifStatement.
    def visitIfStatement(self, ctx:gramatica_v3Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#whileStatement.
    def visitWhileStatement(self, ctx:gramatica_v3Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#forStatement.
    def visitForStatement(self, ctx:gramatica_v3Parser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#forInitDecl.
    def visitForInitDecl(self, ctx:gramatica_v3Parser.ForInitDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#forInitAssign.
    def visitForInitAssign(self, ctx:gramatica_v3Parser.ForInitAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#forUpdate.
    def visitForUpdate(self, ctx:gramatica_v3Parser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#returnStatement.
    def visitReturnStatement(self, ctx:gramatica_v3Parser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#breakStatement.
    def visitBreakStatement(self, ctx:gramatica_v3Parser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#continueStatement.
    def visitContinueStatement(self, ctx:gramatica_v3Parser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#printStatement.
    def visitPrintStatement(self, ctx:gramatica_v3Parser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#exprStatement.
    def visitExprStatement(self, ctx:gramatica_v3Parser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#block.
    def visitBlock(self, ctx:gramatica_v3Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#orExpr.
    def visitOrExpr(self, ctx:gramatica_v3Parser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#funcCallExpr.
    def visitFuncCallExpr(self, ctx:gramatica_v3Parser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#parenExpr.
    def visitParenExpr(self, ctx:gramatica_v3Parser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#numExpr.
    def visitNumExpr(self, ctx:gramatica_v3Parser.NumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#stringExpr.
    def visitStringExpr(self, ctx:gramatica_v3Parser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#floatExpr.
    def visitFloatExpr(self, ctx:gramatica_v3Parser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#notExpr.
    def visitNotExpr(self, ctx:gramatica_v3Parser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#arrayAccessExpr.
    def visitArrayAccessExpr(self, ctx:gramatica_v3Parser.ArrayAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#addExpr.
    def visitAddExpr(self, ctx:gramatica_v3Parser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#negExpr.
    def visitNegExpr(self, ctx:gramatica_v3Parser.NegExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#mulExpr.
    def visitMulExpr(self, ctx:gramatica_v3Parser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#boolExpr.
    def visitBoolExpr(self, ctx:gramatica_v3Parser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#relExpr.
    def visitRelExpr(self, ctx:gramatica_v3Parser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#idExpr.
    def visitIdExpr(self, ctx:gramatica_v3Parser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#andExpr.
    def visitAndExpr(self, ctx:gramatica_v3Parser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#argList.
    def visitArgList(self, ctx:gramatica_v3Parser.ArgListContext):
        return self.visitChildren(ctx)



del gramatica_v3Parser