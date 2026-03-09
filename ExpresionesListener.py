# Generated from Expresiones.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExpresionesParser import ExpresionesParser
else:
    from ExpresionesParser import ExpresionesParser

# This class defines a complete listener for a parse tree produced by ExpresionesParser.
class ExpresionesListener(ParseTreeListener):

    # Enter a parse tree produced by ExpresionesParser#program.
    def enterProgram(self, ctx:ExpresionesParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#program.
    def exitProgram(self, ctx:ExpresionesParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#statement.
    def enterStatement(self, ctx:ExpresionesParser.StatementContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#statement.
    def exitStatement(self, ctx:ExpresionesParser.StatementContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#varDecl.
    def enterVarDecl(self, ctx:ExpresionesParser.VarDeclContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#varDecl.
    def exitVarDecl(self, ctx:ExpresionesParser.VarDeclContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#assignment.
    def enterAssignment(self, ctx:ExpresionesParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#assignment.
    def exitAssignment(self, ctx:ExpresionesParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#exprStatement.
    def enterExprStatement(self, ctx:ExpresionesParser.ExprStatementContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#exprStatement.
    def exitExprStatement(self, ctx:ExpresionesParser.ExprStatementContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#ifStatement.
    def enterIfStatement(self, ctx:ExpresionesParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#ifStatement.
    def exitIfStatement(self, ctx:ExpresionesParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#block.
    def enterBlock(self, ctx:ExpresionesParser.BlockContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#block.
    def exitBlock(self, ctx:ExpresionesParser.BlockContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#t_type.
    def enterT_type(self, ctx:ExpresionesParser.T_typeContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#t_type.
    def exitT_type(self, ctx:ExpresionesParser.T_typeContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#floatExpr.
    def enterFloatExpr(self, ctx:ExpresionesParser.FloatExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#floatExpr.
    def exitFloatExpr(self, ctx:ExpresionesParser.FloatExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#notExpr.
    def enterNotExpr(self, ctx:ExpresionesParser.NotExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#notExpr.
    def exitNotExpr(self, ctx:ExpresionesParser.NotExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#addExpr.
    def enterAddExpr(self, ctx:ExpresionesParser.AddExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#addExpr.
    def exitAddExpr(self, ctx:ExpresionesParser.AddExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#negExpr.
    def enterNegExpr(self, ctx:ExpresionesParser.NegExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#negExpr.
    def exitNegExpr(self, ctx:ExpresionesParser.NegExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#mulExpr.
    def enterMulExpr(self, ctx:ExpresionesParser.MulExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#mulExpr.
    def exitMulExpr(self, ctx:ExpresionesParser.MulExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#orExpr.
    def enterOrExpr(self, ctx:ExpresionesParser.OrExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#orExpr.
    def exitOrExpr(self, ctx:ExpresionesParser.OrExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#boolExpr.
    def enterBoolExpr(self, ctx:ExpresionesParser.BoolExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#boolExpr.
    def exitBoolExpr(self, ctx:ExpresionesParser.BoolExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#relExpr.
    def enterRelExpr(self, ctx:ExpresionesParser.RelExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#relExpr.
    def exitRelExpr(self, ctx:ExpresionesParser.RelExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#parenExpr.
    def enterParenExpr(self, ctx:ExpresionesParser.ParenExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#parenExpr.
    def exitParenExpr(self, ctx:ExpresionesParser.ParenExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#numExpr.
    def enterNumExpr(self, ctx:ExpresionesParser.NumExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#numExpr.
    def exitNumExpr(self, ctx:ExpresionesParser.NumExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#idExpr.
    def enterIdExpr(self, ctx:ExpresionesParser.IdExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#idExpr.
    def exitIdExpr(self, ctx:ExpresionesParser.IdExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#andExpr.
    def enterAndExpr(self, ctx:ExpresionesParser.AndExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#andExpr.
    def exitAndExpr(self, ctx:ExpresionesParser.AndExprContext):
        pass



del ExpresionesParser