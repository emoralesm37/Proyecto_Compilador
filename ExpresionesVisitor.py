# Generated from Expresiones.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpresionesParser import ExpresionesParser
else:
    from ExpresionesParser import ExpresionesParser

# This class defines a complete generic visitor for a parse tree produced by ExpresionesParser.

class ExpresionesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpresionesParser#program.
    def visitProgram(self, ctx:ExpresionesParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#topFuncDecl.
    def visitTopFuncDecl(self, ctx:ExpresionesParser.TopFuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#topStatement.
    def visitTopStatement(self, ctx:ExpresionesParser.TopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#funcDecl.
    def visitFuncDecl(self, ctx:ExpresionesParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#returnType.
    def visitReturnType(self, ctx:ExpresionesParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#paramList.
    def visitParamList(self, ctx:ExpresionesParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#param.
    def visitParam(self, ctx:ExpresionesParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#statement.
    def visitStatement(self, ctx:ExpresionesParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#varDecl.
    def visitVarDecl(self, ctx:ExpresionesParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#assignment.
    def visitAssignment(self, ctx:ExpresionesParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#ifStatement.
    def visitIfStatement(self, ctx:ExpresionesParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#whileStatement.
    def visitWhileStatement(self, ctx:ExpresionesParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#forStatement.
    def visitForStatement(self, ctx:ExpresionesParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#forInitDecl.
    def visitForInitDecl(self, ctx:ExpresionesParser.ForInitDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#forInitAssign.
    def visitForInitAssign(self, ctx:ExpresionesParser.ForInitAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#forUpdate.
    def visitForUpdate(self, ctx:ExpresionesParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#returnStatement.
    def visitReturnStatement(self, ctx:ExpresionesParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#printStatement.
    def visitPrintStatement(self, ctx:ExpresionesParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#exprStatement.
    def visitExprStatement(self, ctx:ExpresionesParser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#block.
    def visitBlock(self, ctx:ExpresionesParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#t_type.
    def visitT_type(self, ctx:ExpresionesParser.T_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#orExpr.
    def visitOrExpr(self, ctx:ExpresionesParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#funcCallExpr.
    def visitFuncCallExpr(self, ctx:ExpresionesParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#parenExpr.
    def visitParenExpr(self, ctx:ExpresionesParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#numExpr.
    def visitNumExpr(self, ctx:ExpresionesParser.NumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#stringExpr.
    def visitStringExpr(self, ctx:ExpresionesParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#floatExpr.
    def visitFloatExpr(self, ctx:ExpresionesParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#notExpr.
    def visitNotExpr(self, ctx:ExpresionesParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#addExpr.
    def visitAddExpr(self, ctx:ExpresionesParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#negExpr.
    def visitNegExpr(self, ctx:ExpresionesParser.NegExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#mulExpr.
    def visitMulExpr(self, ctx:ExpresionesParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#boolExpr.
    def visitBoolExpr(self, ctx:ExpresionesParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#relExpr.
    def visitRelExpr(self, ctx:ExpresionesParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#idExpr.
    def visitIdExpr(self, ctx:ExpresionesParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#andExpr.
    def visitAndExpr(self, ctx:ExpresionesParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#argList.
    def visitArgList(self, ctx:ExpresionesParser.ArgListContext):
        return self.visitChildren(ctx)



del ExpresionesParser