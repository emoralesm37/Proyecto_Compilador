# Generated from gramatica_v4.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramatica_v4Parser import gramatica_v4Parser
else:
    from gramatica_v4Parser import gramatica_v4Parser

# This class defines a complete listener for a parse tree produced by gramatica_v4Parser.
class gramatica_v4Listener(ParseTreeListener):

    # Enter a parse tree produced by gramatica_v4Parser#program.
    def enterProgram(self, ctx:gramatica_v4Parser.ProgramContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#program.
    def exitProgram(self, ctx:gramatica_v4Parser.ProgramContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#topFuncDecl.
    def enterTopFuncDecl(self, ctx:gramatica_v4Parser.TopFuncDeclContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#topFuncDecl.
    def exitTopFuncDecl(self, ctx:gramatica_v4Parser.TopFuncDeclContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#topImport.
    def enterTopImport(self, ctx:gramatica_v4Parser.TopImportContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#topImport.
    def exitTopImport(self, ctx:gramatica_v4Parser.TopImportContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#topStructDecl.
    def enterTopStructDecl(self, ctx:gramatica_v4Parser.TopStructDeclContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#topStructDecl.
    def exitTopStructDecl(self, ctx:gramatica_v4Parser.TopStructDeclContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#topStatement.
    def enterTopStatement(self, ctx:gramatica_v4Parser.TopStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#topStatement.
    def exitTopStatement(self, ctx:gramatica_v4Parser.TopStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#importDecl.
    def enterImportDecl(self, ctx:gramatica_v4Parser.ImportDeclContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#importDecl.
    def exitImportDecl(self, ctx:gramatica_v4Parser.ImportDeclContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#structDecl.
    def enterStructDecl(self, ctx:gramatica_v4Parser.StructDeclContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#structDecl.
    def exitStructDecl(self, ctx:gramatica_v4Parser.StructDeclContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#structField.
    def enterStructField(self, ctx:gramatica_v4Parser.StructFieldContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#structField.
    def exitStructField(self, ctx:gramatica_v4Parser.StructFieldContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#funcDecl.
    def enterFuncDecl(self, ctx:gramatica_v4Parser.FuncDeclContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#funcDecl.
    def exitFuncDecl(self, ctx:gramatica_v4Parser.FuncDeclContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#returnType.
    def enterReturnType(self, ctx:gramatica_v4Parser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#returnType.
    def exitReturnType(self, ctx:gramatica_v4Parser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#paramList.
    def enterParamList(self, ctx:gramatica_v4Parser.ParamListContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#paramList.
    def exitParamList(self, ctx:gramatica_v4Parser.ParamListContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#param.
    def enterParam(self, ctx:gramatica_v4Parser.ParamContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#param.
    def exitParam(self, ctx:gramatica_v4Parser.ParamContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#t_type.
    def enterT_type(self, ctx:gramatica_v4Parser.T_typeContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#t_type.
    def exitT_type(self, ctx:gramatica_v4Parser.T_typeContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#intArrayType.
    def enterIntArrayType(self, ctx:gramatica_v4Parser.IntArrayTypeContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#intArrayType.
    def exitIntArrayType(self, ctx:gramatica_v4Parser.IntArrayTypeContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#floatArrayType.
    def enterFloatArrayType(self, ctx:gramatica_v4Parser.FloatArrayTypeContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#floatArrayType.
    def exitFloatArrayType(self, ctx:gramatica_v4Parser.FloatArrayTypeContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#boolArrayType.
    def enterBoolArrayType(self, ctx:gramatica_v4Parser.BoolArrayTypeContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#boolArrayType.
    def exitBoolArrayType(self, ctx:gramatica_v4Parser.BoolArrayTypeContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#stringArrayType.
    def enterStringArrayType(self, ctx:gramatica_v4Parser.StringArrayTypeContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#stringArrayType.
    def exitStringArrayType(self, ctx:gramatica_v4Parser.StringArrayTypeContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#statement.
    def enterStatement(self, ctx:gramatica_v4Parser.StatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#statement.
    def exitStatement(self, ctx:gramatica_v4Parser.StatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#varDecl.
    def enterVarDecl(self, ctx:gramatica_v4Parser.VarDeclContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#varDecl.
    def exitVarDecl(self, ctx:gramatica_v4Parser.VarDeclContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#arrayDecl.
    def enterArrayDecl(self, ctx:gramatica_v4Parser.ArrayDeclContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#arrayDecl.
    def exitArrayDecl(self, ctx:gramatica_v4Parser.ArrayDeclContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#structVarDecl.
    def enterStructVarDecl(self, ctx:gramatica_v4Parser.StructVarDeclContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#structVarDecl.
    def exitStructVarDecl(self, ctx:gramatica_v4Parser.StructVarDeclContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#arrayLiteral.
    def enterArrayLiteral(self, ctx:gramatica_v4Parser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#arrayLiteral.
    def exitArrayLiteral(self, ctx:gramatica_v4Parser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#assignment.
    def enterAssignment(self, ctx:gramatica_v4Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#assignment.
    def exitAssignment(self, ctx:gramatica_v4Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#fieldAssign.
    def enterFieldAssign(self, ctx:gramatica_v4Parser.FieldAssignContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#fieldAssign.
    def exitFieldAssign(self, ctx:gramatica_v4Parser.FieldAssignContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#arrayAssign.
    def enterArrayAssign(self, ctx:gramatica_v4Parser.ArrayAssignContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#arrayAssign.
    def exitArrayAssign(self, ctx:gramatica_v4Parser.ArrayAssignContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#ifStatement.
    def enterIfStatement(self, ctx:gramatica_v4Parser.IfStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#ifStatement.
    def exitIfStatement(self, ctx:gramatica_v4Parser.IfStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#whileStatement.
    def enterWhileStatement(self, ctx:gramatica_v4Parser.WhileStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#whileStatement.
    def exitWhileStatement(self, ctx:gramatica_v4Parser.WhileStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#forStatement.
    def enterForStatement(self, ctx:gramatica_v4Parser.ForStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#forStatement.
    def exitForStatement(self, ctx:gramatica_v4Parser.ForStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#switchStatement.
    def enterSwitchStatement(self, ctx:gramatica_v4Parser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#switchStatement.
    def exitSwitchStatement(self, ctx:gramatica_v4Parser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#caseClause.
    def enterCaseClause(self, ctx:gramatica_v4Parser.CaseClauseContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#caseClause.
    def exitCaseClause(self, ctx:gramatica_v4Parser.CaseClauseContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#defaultClause.
    def enterDefaultClause(self, ctx:gramatica_v4Parser.DefaultClauseContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#defaultClause.
    def exitDefaultClause(self, ctx:gramatica_v4Parser.DefaultClauseContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#forInitDecl.
    def enterForInitDecl(self, ctx:gramatica_v4Parser.ForInitDeclContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#forInitDecl.
    def exitForInitDecl(self, ctx:gramatica_v4Parser.ForInitDeclContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#forInitAssign.
    def enterForInitAssign(self, ctx:gramatica_v4Parser.ForInitAssignContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#forInitAssign.
    def exitForInitAssign(self, ctx:gramatica_v4Parser.ForInitAssignContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#forUpdate.
    def enterForUpdate(self, ctx:gramatica_v4Parser.ForUpdateContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#forUpdate.
    def exitForUpdate(self, ctx:gramatica_v4Parser.ForUpdateContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#returnStatement.
    def enterReturnStatement(self, ctx:gramatica_v4Parser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#returnStatement.
    def exitReturnStatement(self, ctx:gramatica_v4Parser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#breakStatement.
    def enterBreakStatement(self, ctx:gramatica_v4Parser.BreakStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#breakStatement.
    def exitBreakStatement(self, ctx:gramatica_v4Parser.BreakStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#continueStatement.
    def enterContinueStatement(self, ctx:gramatica_v4Parser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#continueStatement.
    def exitContinueStatement(self, ctx:gramatica_v4Parser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#printStatement.
    def enterPrintStatement(self, ctx:gramatica_v4Parser.PrintStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#printStatement.
    def exitPrintStatement(self, ctx:gramatica_v4Parser.PrintStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#exprStatement.
    def enterExprStatement(self, ctx:gramatica_v4Parser.ExprStatementContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#exprStatement.
    def exitExprStatement(self, ctx:gramatica_v4Parser.ExprStatementContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#block.
    def enterBlock(self, ctx:gramatica_v4Parser.BlockContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#block.
    def exitBlock(self, ctx:gramatica_v4Parser.BlockContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#castExpr.
    def enterCastExpr(self, ctx:gramatica_v4Parser.CastExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#castExpr.
    def exitCastExpr(self, ctx:gramatica_v4Parser.CastExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#fieldAccessExpr.
    def enterFieldAccessExpr(self, ctx:gramatica_v4Parser.FieldAccessExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#fieldAccessExpr.
    def exitFieldAccessExpr(self, ctx:gramatica_v4Parser.FieldAccessExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#orExpr.
    def enterOrExpr(self, ctx:gramatica_v4Parser.OrExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#orExpr.
    def exitOrExpr(self, ctx:gramatica_v4Parser.OrExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#funcCallExpr.
    def enterFuncCallExpr(self, ctx:gramatica_v4Parser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#funcCallExpr.
    def exitFuncCallExpr(self, ctx:gramatica_v4Parser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#parenExpr.
    def enterParenExpr(self, ctx:gramatica_v4Parser.ParenExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#parenExpr.
    def exitParenExpr(self, ctx:gramatica_v4Parser.ParenExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#numExpr.
    def enterNumExpr(self, ctx:gramatica_v4Parser.NumExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#numExpr.
    def exitNumExpr(self, ctx:gramatica_v4Parser.NumExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#stringExpr.
    def enterStringExpr(self, ctx:gramatica_v4Parser.StringExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#stringExpr.
    def exitStringExpr(self, ctx:gramatica_v4Parser.StringExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#floatExpr.
    def enterFloatExpr(self, ctx:gramatica_v4Parser.FloatExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#floatExpr.
    def exitFloatExpr(self, ctx:gramatica_v4Parser.FloatExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#notExpr.
    def enterNotExpr(self, ctx:gramatica_v4Parser.NotExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#notExpr.
    def exitNotExpr(self, ctx:gramatica_v4Parser.NotExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#arrayAccessExpr.
    def enterArrayAccessExpr(self, ctx:gramatica_v4Parser.ArrayAccessExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#arrayAccessExpr.
    def exitArrayAccessExpr(self, ctx:gramatica_v4Parser.ArrayAccessExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#ternaryExpr.
    def enterTernaryExpr(self, ctx:gramatica_v4Parser.TernaryExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#ternaryExpr.
    def exitTernaryExpr(self, ctx:gramatica_v4Parser.TernaryExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#addExpr.
    def enterAddExpr(self, ctx:gramatica_v4Parser.AddExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#addExpr.
    def exitAddExpr(self, ctx:gramatica_v4Parser.AddExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#negExpr.
    def enterNegExpr(self, ctx:gramatica_v4Parser.NegExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#negExpr.
    def exitNegExpr(self, ctx:gramatica_v4Parser.NegExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#mulExpr.
    def enterMulExpr(self, ctx:gramatica_v4Parser.MulExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#mulExpr.
    def exitMulExpr(self, ctx:gramatica_v4Parser.MulExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#boolExpr.
    def enterBoolExpr(self, ctx:gramatica_v4Parser.BoolExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#boolExpr.
    def exitBoolExpr(self, ctx:gramatica_v4Parser.BoolExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#relExpr.
    def enterRelExpr(self, ctx:gramatica_v4Parser.RelExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#relExpr.
    def exitRelExpr(self, ctx:gramatica_v4Parser.RelExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#idExpr.
    def enterIdExpr(self, ctx:gramatica_v4Parser.IdExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#idExpr.
    def exitIdExpr(self, ctx:gramatica_v4Parser.IdExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#andExpr.
    def enterAndExpr(self, ctx:gramatica_v4Parser.AndExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#andExpr.
    def exitAndExpr(self, ctx:gramatica_v4Parser.AndExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#argList.
    def enterArgList(self, ctx:gramatica_v4Parser.ArgListContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#argList.
    def exitArgList(self, ctx:gramatica_v4Parser.ArgListContext):
        pass



del gramatica_v4Parser