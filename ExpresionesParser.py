# Generated from Expresiones.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,34,103,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,55,8,5,1,6,1,6,5,
        6,59,8,6,10,6,12,6,62,9,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,81,8,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,98,8,8,10,8,12,8,101,9,8,
        1,8,0,1,16,9,0,2,4,6,8,10,12,14,16,0,4,1,0,4,7,1,0,11,12,1,0,9,10,
        1,0,13,18,110,0,18,1,0,0,0,2,33,1,0,0,0,4,35,1,0,0,0,6,39,1,0,0,
        0,8,44,1,0,0,0,10,47,1,0,0,0,12,56,1,0,0,0,14,65,1,0,0,0,16,80,1,
        0,0,0,18,19,5,3,0,0,19,23,5,25,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,
        25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,
        0,26,27,5,26,0,0,27,28,5,0,0,1,28,1,1,0,0,0,29,34,3,4,2,0,30,34,
        3,6,3,0,31,34,3,10,5,0,32,34,3,8,4,0,33,29,1,0,0,0,33,30,1,0,0,0,
        33,31,1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,35,36,3,14,7,0,36,37,5,
        32,0,0,37,38,5,29,0,0,38,5,1,0,0,0,39,40,5,32,0,0,40,41,5,22,0,0,
        41,42,3,16,8,0,42,43,5,29,0,0,43,7,1,0,0,0,44,45,3,16,8,0,45,46,
        5,29,0,0,46,9,1,0,0,0,47,48,5,1,0,0,48,49,5,23,0,0,49,50,3,16,8,
        0,50,51,5,24,0,0,51,54,3,12,6,0,52,53,5,2,0,0,53,55,3,12,6,0,54,
        52,1,0,0,0,54,55,1,0,0,0,55,11,1,0,0,0,56,60,5,25,0,0,57,59,3,2,
        1,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,
        1,0,0,0,62,60,1,0,0,0,63,64,5,26,0,0,64,13,1,0,0,0,65,66,7,0,0,0,
        66,15,1,0,0,0,67,68,6,8,-1,0,68,69,5,21,0,0,69,81,3,16,8,7,70,71,
        5,10,0,0,71,81,3,16,8,6,72,73,5,23,0,0,73,74,3,16,8,0,74,75,5,24,
        0,0,75,81,1,0,0,0,76,81,5,30,0,0,77,81,5,31,0,0,78,81,5,8,0,0,79,
        81,5,32,0,0,80,67,1,0,0,0,80,70,1,0,0,0,80,72,1,0,0,0,80,76,1,0,
        0,0,80,77,1,0,0,0,80,78,1,0,0,0,80,79,1,0,0,0,81,99,1,0,0,0,82,83,
        10,12,0,0,83,84,7,1,0,0,84,98,3,16,8,13,85,86,10,11,0,0,86,87,7,
        2,0,0,87,98,3,16,8,12,88,89,10,10,0,0,89,90,7,3,0,0,90,98,3,16,8,
        11,91,92,10,9,0,0,92,93,5,19,0,0,93,98,3,16,8,10,94,95,10,8,0,0,
        95,96,5,20,0,0,96,98,3,16,8,9,97,82,1,0,0,0,97,85,1,0,0,0,97,88,
        1,0,0,0,97,91,1,0,0,0,97,94,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,
        99,100,1,0,0,0,100,17,1,0,0,0,101,99,1,0,0,0,7,23,33,54,60,80,97,
        99
    ]

class ExpresionesParser ( Parser ):

    grammarFileName = "Expresiones.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'program'", "'int'", 
                     "'float'", "'bool'", "'string'", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'/'", "'=='", "<INVALID>", "'<='", "'>='", 
                     "'<'", "'>'", "'&&'", "'||'", "'!'", "'='", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "PROGRAM", "INT_T", "FLOAT_T", 
                      "BOOL_T", "STRING_T", "BOOL_LIT", "PLUS", "MINUS", 
                      "TIMES", "DIV", "EQ", "NEQ", "LEQ", "GEQ", "LT", "GT", 
                      "AND", "OR", "NOT", "ASSIGN", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEMI", 
                      "FLOAT_LIT", "NUM", "ID", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDecl = 2
    RULE_assignment = 3
    RULE_exprStatement = 4
    RULE_ifStatement = 5
    RULE_block = 6
    RULE_type = 7
    RULE_expr = 8

    ruleNames =  [ "program", "statement", "varDecl", "assignment", "exprStatement", 
                   "ifStatement", "block", "type", "expr" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    PROGRAM=3
    INT_T=4
    FLOAT_T=5
    BOOL_T=6
    STRING_T=7
    BOOL_LIT=8
    PLUS=9
    MINUS=10
    TIMES=11
    DIV=12
    EQ=13
    NEQ=14
    LEQ=15
    GEQ=16
    LT=17
    GT=18
    AND=19
    OR=20
    NOT=21
    ASSIGN=22
    LPAREN=23
    RPAREN=24
    LBRACE=25
    RBRACE=26
    LBRACKET=27
    RBRACKET=28
    SEMI=29
    FLOAT_LIT=30
    NUM=31
    ID=32
    WS=33
    COMMENT=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(ExpresionesParser.PROGRAM, 0)

        def LBRACE(self):
            return self.getToken(ExpresionesParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ExpresionesParser.RBRACE, 0)

        def EOF(self):
            return self.getToken(ExpresionesParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpresionesParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExpresionesParser.StatementContext,i)


        def getRuleIndex(self):
            return ExpresionesParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ExpresionesParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(ExpresionesParser.PROGRAM)
            self.state = 19
            self.match(ExpresionesParser.LBRACE)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7526680050) != 0):
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(ExpresionesParser.RBRACE)
            self.state = 27
            self.match(ExpresionesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(ExpresionesParser.VarDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(ExpresionesParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ExpresionesParser.IfStatementContext,0)


        def exprStatement(self):
            return self.getTypedRuleContext(ExpresionesParser.ExprStatementContext,0)


        def getRuleIndex(self):
            return ExpresionesParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ExpresionesParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.exprStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(ExpresionesParser.TypeContext,0)


        def ID(self):
            return self.getToken(ExpresionesParser.ID, 0)

        def SEMI(self):
            return self.getToken(ExpresionesParser.SEMI, 0)

        def getRuleIndex(self):
            return ExpresionesParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = ExpresionesParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.type_()
            self.state = 36
            self.match(ExpresionesParser.ID)
            self.state = 37
            self.match(ExpresionesParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExpresionesParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ExpresionesParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExpresionesParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(ExpresionesParser.SEMI, 0)

        def getRuleIndex(self):
            return ExpresionesParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ExpresionesParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(ExpresionesParser.ID)
            self.state = 40
            self.match(ExpresionesParser.ASSIGN)
            self.state = 41
            self.expr(0)
            self.state = 42
            self.match(ExpresionesParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExpresionesParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(ExpresionesParser.SEMI, 0)

        def getRuleIndex(self):
            return ExpresionesParser.RULE_exprStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStatement" ):
                listener.enterExprStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStatement" ):
                listener.exitExprStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStatement" ):
                return visitor.visitExprStatement(self)
            else:
                return visitor.visitChildren(self)




    def exprStatement(self):

        localctx = ExpresionesParser.ExprStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exprStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.expr(0)
            self.state = 45
            self.match(ExpresionesParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExpresionesParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ExpresionesParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExpresionesParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ExpresionesParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpresionesParser.BlockContext)
            else:
                return self.getTypedRuleContext(ExpresionesParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(ExpresionesParser.ELSE, 0)

        def getRuleIndex(self):
            return ExpresionesParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = ExpresionesParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(ExpresionesParser.IF)
            self.state = 48
            self.match(ExpresionesParser.LPAREN)
            self.state = 49
            self.expr(0)
            self.state = 50
            self.match(ExpresionesParser.RPAREN)
            self.state = 51
            self.block()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 52
                self.match(ExpresionesParser.ELSE)
                self.state = 53
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ExpresionesParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ExpresionesParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpresionesParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExpresionesParser.StatementContext,i)


        def getRuleIndex(self):
            return ExpresionesParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ExpresionesParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(ExpresionesParser.LBRACE)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7526680050) != 0):
                self.state = 57
                self.statement()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(ExpresionesParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_T(self):
            return self.getToken(ExpresionesParser.INT_T, 0)

        def FLOAT_T(self):
            return self.getToken(ExpresionesParser.FLOAT_T, 0)

        def BOOL_T(self):
            return self.getToken(ExpresionesParser.BOOL_T, 0)

        def STRING_T(self):
            return self.getToken(ExpresionesParser.STRING_T, 0)

        def getRuleIndex(self):
            return ExpresionesParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = ExpresionesParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 240) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExpresionesParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class FloatExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_LIT(self):
            return self.getToken(ExpresionesParser.FLOAT_LIT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatExpr" ):
                listener.enterFloatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatExpr" ):
                listener.exitFloatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(ExpresionesParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(ExpresionesParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpresionesParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExpresionesParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(ExpresionesParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(ExpresionesParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(ExpresionesParser.MINUS, 0)
        def expr(self):
            return self.getTypedRuleContext(ExpresionesParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegExpr" ):
                listener.enterNegExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegExpr" ):
                listener.exitNegExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegExpr" ):
                return visitor.visitNegExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpresionesParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExpresionesParser.ExprContext,i)

        def TIMES(self):
            return self.getToken(ExpresionesParser.TIMES, 0)
        def DIV(self):
            return self.getToken(ExpresionesParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpresionesParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExpresionesParser.ExprContext,i)

        def OR(self):
            return self.getToken(ExpresionesParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class BoolExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_LIT(self):
            return self.getToken(ExpresionesParser.BOOL_LIT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpr" ):
                listener.enterBoolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpr" ):
                listener.exitBoolExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpresionesParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExpresionesParser.ExprContext,i)

        def EQ(self):
            return self.getToken(ExpresionesParser.EQ, 0)
        def NEQ(self):
            return self.getToken(ExpresionesParser.NEQ, 0)
        def LT(self):
            return self.getToken(ExpresionesParser.LT, 0)
        def GT(self):
            return self.getToken(ExpresionesParser.GT, 0)
        def LEQ(self):
            return self.getToken(ExpresionesParser.LEQ, 0)
        def GEQ(self):
            return self.getToken(ExpresionesParser.GEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelExpr" ):
                listener.enterRelExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelExpr" ):
                listener.exitRelExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ExpresionesParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(ExpresionesParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(ExpresionesParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ExpresionesParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumExpr" ):
                listener.enterNumExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumExpr" ):
                listener.exitNumExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumExpr" ):
                return visitor.visitNumExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExpresionesParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpresionesParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExpresionesParser.ExprContext,i)

        def AND(self):
            return self.getToken(ExpresionesParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpresionesParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                localctx = ExpresionesParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 68
                self.match(ExpresionesParser.NOT)
                self.state = 69
                self.expr(7)
                pass
            elif token in [10]:
                localctx = ExpresionesParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 70
                self.match(ExpresionesParser.MINUS)
                self.state = 71
                self.expr(6)
                pass
            elif token in [23]:
                localctx = ExpresionesParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                self.match(ExpresionesParser.LPAREN)
                self.state = 73
                self.expr(0)
                self.state = 74
                self.match(ExpresionesParser.RPAREN)
                pass
            elif token in [30]:
                localctx = ExpresionesParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                self.match(ExpresionesParser.FLOAT_LIT)
                pass
            elif token in [31]:
                localctx = ExpresionesParser.NumExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 77
                self.match(ExpresionesParser.NUM)
                pass
            elif token in [8]:
                localctx = ExpresionesParser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 78
                self.match(ExpresionesParser.BOOL_LIT)
                pass
            elif token in [32]:
                localctx = ExpresionesParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 79
                self.match(ExpresionesParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 99
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 97
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ExpresionesParser.MulExprContext(self, ExpresionesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 82
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 83
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 84
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = ExpresionesParser.AddExprContext(self, ExpresionesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 86
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 87
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = ExpresionesParser.RelExprContext(self, ExpresionesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 88
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 89
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 90
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = ExpresionesParser.AndExprContext(self, ExpresionesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 91
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 92
                        self.match(ExpresionesParser.AND)
                        self.state = 93
                        self.expr(10)
                        pass

                    elif la_ == 5:
                        localctx = ExpresionesParser.OrExprContext(self, ExpresionesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 94
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 95
                        self.match(ExpresionesParser.OR)
                        self.state = 96
                        self.expr(9)
                        pass

             
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         




