# Generated from Expresiones.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3$")
        buf.write("i\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\7\2\30\n\2\f\2\16\2\33")
        buf.write("\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3$\n\3\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\79\n\7\3\b\3\b\7\b=\n\b\f\b\16\b@\13\b\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\5\nS\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\nd\n\n\f\n\16\ng\13\n\3")
        buf.write("\n\2\3\22\13\2\4\6\b\n\f\16\20\22\2\6\3\2\6\t\3\2\17\24")
        buf.write("\3\2\13\f\3\2\r\16\2p\2\24\3\2\2\2\4#\3\2\2\2\6%\3\2\2")
        buf.write("\2\b)\3\2\2\2\n.\3\2\2\2\f\61\3\2\2\2\16:\3\2\2\2\20C")
        buf.write("\3\2\2\2\22R\3\2\2\2\24\25\7\5\2\2\25\31\7\33\2\2\26\30")
        buf.write("\5\4\3\2\27\26\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31")
        buf.write("\32\3\2\2\2\32\34\3\2\2\2\33\31\3\2\2\2\34\35\7\34\2\2")
        buf.write("\35\36\7\2\2\3\36\3\3\2\2\2\37$\5\6\4\2 $\5\b\5\2!$\5")
        buf.write("\f\7\2\"$\5\n\6\2#\37\3\2\2\2# \3\2\2\2#!\3\2\2\2#\"\3")
        buf.write("\2\2\2$\5\3\2\2\2%&\5\20\t\2&\'\7\"\2\2\'(\7\37\2\2(\7")
        buf.write("\3\2\2\2)*\7\"\2\2*+\7\30\2\2+,\5\22\n\2,-\7\37\2\2-\t")
        buf.write("\3\2\2\2./\5\22\n\2/\60\7\37\2\2\60\13\3\2\2\2\61\62\7")
        buf.write("\3\2\2\62\63\7\31\2\2\63\64\5\22\n\2\64\65\7\32\2\2\65")
        buf.write("8\5\16\b\2\66\67\7\4\2\2\679\5\16\b\28\66\3\2\2\289\3")
        buf.write("\2\2\29\r\3\2\2\2:>\7\33\2\2;=\5\4\3\2<;\3\2\2\2=@\3\2")
        buf.write("\2\2><\3\2\2\2>?\3\2\2\2?A\3\2\2\2@>\3\2\2\2AB\7\34\2")
        buf.write("\2B\17\3\2\2\2CD\t\2\2\2D\21\3\2\2\2EF\b\n\1\2FG\7\27")
        buf.write("\2\2GS\5\22\n\tHI\7\f\2\2IS\5\22\n\bJK\7\31\2\2KL\5\22")
        buf.write("\n\2LM\7\32\2\2MS\3\2\2\2NS\7 \2\2OS\7!\2\2PS\7\n\2\2")
        buf.write("QS\7\"\2\2RE\3\2\2\2RH\3\2\2\2RJ\3\2\2\2RN\3\2\2\2RO\3")
        buf.write("\2\2\2RP\3\2\2\2RQ\3\2\2\2Se\3\2\2\2TU\f\16\2\2UV\7\26")
        buf.write("\2\2Vd\5\22\n\17WX\f\r\2\2XY\7\25\2\2Yd\5\22\n\16Z[\f")
        buf.write("\f\2\2[\\\t\3\2\2\\d\5\22\n\r]^\f\13\2\2^_\t\4\2\2_d\5")
        buf.write("\22\n\f`a\f\n\2\2ab\t\5\2\2bd\5\22\n\13cT\3\2\2\2cW\3")
        buf.write("\2\2\2cZ\3\2\2\2c]\3\2\2\2c`\3\2\2\2dg\3\2\2\2ec\3\2\2")
        buf.write("\2ef\3\2\2\2f\23\3\2\2\2ge\3\2\2\2\t\31#8>Rce")
        return buf.getvalue()


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
    RULE_t_type = 7
    RULE_expr = 8

    ruleNames =  [ "program", "statement", "varDecl", "assignment", "exprStatement", 
                   "ifStatement", "block", "t_type", "expr" ]

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
        self.checkVersion("4.9.2")
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpresionesParser.IF) | (1 << ExpresionesParser.INT_T) | (1 << ExpresionesParser.FLOAT_T) | (1 << ExpresionesParser.BOOL_T) | (1 << ExpresionesParser.STRING_T) | (1 << ExpresionesParser.BOOL_LIT) | (1 << ExpresionesParser.MINUS) | (1 << ExpresionesParser.NOT) | (1 << ExpresionesParser.LPAREN) | (1 << ExpresionesParser.FLOAT_LIT) | (1 << ExpresionesParser.NUM) | (1 << ExpresionesParser.ID))) != 0):
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

        def t_type(self):
            return self.getTypedRuleContext(ExpresionesParser.T_typeContext,0)


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
            self.t_type()
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
            if _la==ExpresionesParser.ELSE:
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpresionesParser.IF) | (1 << ExpresionesParser.INT_T) | (1 << ExpresionesParser.FLOAT_T) | (1 << ExpresionesParser.BOOL_T) | (1 << ExpresionesParser.STRING_T) | (1 << ExpresionesParser.BOOL_LIT) | (1 << ExpresionesParser.MINUS) | (1 << ExpresionesParser.NOT) | (1 << ExpresionesParser.LPAREN) | (1 << ExpresionesParser.FLOAT_LIT) | (1 << ExpresionesParser.NUM) | (1 << ExpresionesParser.ID))) != 0):
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

    class T_typeContext(ParserRuleContext):
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
            return ExpresionesParser.RULE_t_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_type" ):
                listener.enterT_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_type" ):
                listener.exitT_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_type" ):
                return visitor.visitT_type(self)
            else:
                return visitor.visitChildren(self)




    def t_type(self):

        localctx = ExpresionesParser.T_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_t_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpresionesParser.INT_T) | (1 << ExpresionesParser.FLOAT_T) | (1 << ExpresionesParser.BOOL_T) | (1 << ExpresionesParser.STRING_T))) != 0)):
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
            if token in [ExpresionesParser.NOT]:
                localctx = ExpresionesParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 68
                self.match(ExpresionesParser.NOT)
                self.state = 69
                self.expr(7)
                pass
            elif token in [ExpresionesParser.MINUS]:
                localctx = ExpresionesParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 70
                self.match(ExpresionesParser.MINUS)
                self.state = 71
                self.expr(6)
                pass
            elif token in [ExpresionesParser.LPAREN]:
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
            elif token in [ExpresionesParser.FLOAT_LIT]:
                localctx = ExpresionesParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                self.match(ExpresionesParser.FLOAT_LIT)
                pass
            elif token in [ExpresionesParser.NUM]:
                localctx = ExpresionesParser.NumExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 77
                self.match(ExpresionesParser.NUM)
                pass
            elif token in [ExpresionesParser.BOOL_LIT]:
                localctx = ExpresionesParser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 78
                self.match(ExpresionesParser.BOOL_LIT)
                pass
            elif token in [ExpresionesParser.ID]:
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
                        localctx = ExpresionesParser.OrExprContext(self, ExpresionesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 82
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 83
                        self.match(ExpresionesParser.OR)
                        self.state = 84
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = ExpresionesParser.AndExprContext(self, ExpresionesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 86
                        self.match(ExpresionesParser.AND)
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
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExpresionesParser.EQ) | (1 << ExpresionesParser.NEQ) | (1 << ExpresionesParser.LEQ) | (1 << ExpresionesParser.GEQ) | (1 << ExpresionesParser.LT) | (1 << ExpresionesParser.GT))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 90
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = ExpresionesParser.AddExprContext(self, ExpresionesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 91
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 92
                        _la = self._input.LA(1)
                        if not(_la==ExpresionesParser.PLUS or _la==ExpresionesParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 93
                        self.expr(10)
                        pass

                    elif la_ == 5:
                        localctx = ExpresionesParser.MulExprContext(self, ExpresionesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 94
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 95
                        _la = self._input.LA(1)
                        if not(_la==ExpresionesParser.TIMES or _la==ExpresionesParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
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
         




