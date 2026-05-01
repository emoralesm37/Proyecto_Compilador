# Generated from gramatica_v3.g4 by ANTLR 4.13.2
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
        4,1,46,305,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,3,0,59,8,0,1,0,1,0,4,0,63,8,0,11,0,12,0,64,1,0,
        1,0,1,0,1,1,1,1,1,1,3,1,73,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,
        3,83,8,3,1,3,1,3,1,3,1,4,1,4,1,4,3,4,91,8,4,1,5,1,5,1,5,5,5,96,8,
        5,10,5,12,5,99,9,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,107,8,6,1,7,1,7,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,123,8,8,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,137,8,9,1,10,1,10,
        1,10,1,10,3,10,143,8,10,1,10,1,10,1,11,1,11,1,11,1,11,3,11,151,8,
        11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,159,8,12,10,12,12,12,162,9,
        12,3,12,164,8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,
        15,188,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,3,18,214,8,18,1,19,1,19,1,19,1,19,1,20,1,20,3,20,222,8,20,1,20,
        1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,
        1,24,1,24,1,24,1,25,1,25,5,25,243,8,25,10,25,12,25,246,9,25,1,25,
        1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,3,26,263,8,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,3,26,275,8,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,5,26,292,8,26,10,26,12,26,295,9,26,
        1,27,1,27,1,27,5,27,300,8,27,10,27,12,27,303,9,27,1,27,0,1,52,28,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,0,4,1,0,12,15,1,0,19,21,1,0,17,18,1,0,22,27,323,0,
        56,1,0,0,0,2,72,1,0,0,0,4,74,1,0,0,0,6,78,1,0,0,0,8,90,1,0,0,0,10,
        92,1,0,0,0,12,106,1,0,0,0,14,108,1,0,0,0,16,122,1,0,0,0,18,136,1,
        0,0,0,20,138,1,0,0,0,22,146,1,0,0,0,24,154,1,0,0,0,26,167,1,0,0,
        0,28,172,1,0,0,0,30,180,1,0,0,0,32,189,1,0,0,0,34,195,1,0,0,0,36,
        213,1,0,0,0,38,215,1,0,0,0,40,219,1,0,0,0,42,225,1,0,0,0,44,228,
        1,0,0,0,46,231,1,0,0,0,48,237,1,0,0,0,50,240,1,0,0,0,52,274,1,0,
        0,0,54,296,1,0,0,0,56,58,5,9,0,0,57,59,5,43,0,0,58,57,1,0,0,0,58,
        59,1,0,0,0,59,60,1,0,0,0,60,62,5,34,0,0,61,63,3,2,1,0,62,61,1,0,
        0,0,63,64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,66,1,0,0,0,66,67,
        5,35,0,0,67,68,5,0,0,1,68,1,1,0,0,0,69,73,3,6,3,0,70,73,3,4,2,0,
        71,73,3,18,9,0,72,69,1,0,0,0,72,70,1,0,0,0,72,71,1,0,0,0,73,3,1,
        0,0,0,74,75,5,10,0,0,75,76,5,43,0,0,76,77,5,38,0,0,77,5,1,0,0,0,
        78,79,3,8,4,0,79,80,5,43,0,0,80,82,5,32,0,0,81,83,3,10,5,0,82,81,
        1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,85,5,33,0,0,85,86,3,50,25,
        0,86,7,1,0,0,0,87,91,3,14,7,0,88,91,3,16,8,0,89,91,5,11,0,0,90,87,
        1,0,0,0,90,88,1,0,0,0,90,89,1,0,0,0,91,9,1,0,0,0,92,97,3,12,6,0,
        93,94,5,39,0,0,94,96,3,12,6,0,95,93,1,0,0,0,96,99,1,0,0,0,97,95,
        1,0,0,0,97,98,1,0,0,0,98,11,1,0,0,0,99,97,1,0,0,0,100,101,3,14,7,
        0,101,102,5,43,0,0,102,107,1,0,0,0,103,104,3,16,8,0,104,105,5,43,
        0,0,105,107,1,0,0,0,106,100,1,0,0,0,106,103,1,0,0,0,107,13,1,0,0,
        0,108,109,7,0,0,0,109,15,1,0,0,0,110,111,5,12,0,0,111,112,5,36,0,
        0,112,123,5,37,0,0,113,114,5,13,0,0,114,115,5,36,0,0,115,123,5,37,
        0,0,116,117,5,14,0,0,117,118,5,36,0,0,118,123,5,37,0,0,119,120,5,
        15,0,0,120,121,5,36,0,0,121,123,5,37,0,0,122,110,1,0,0,0,122,113,
        1,0,0,0,122,116,1,0,0,0,122,119,1,0,0,0,123,17,1,0,0,0,124,137,3,
        20,10,0,125,137,3,22,11,0,126,137,3,26,13,0,127,137,3,28,14,0,128,
        137,3,30,15,0,129,137,3,32,16,0,130,137,3,34,17,0,131,137,3,40,20,
        0,132,137,3,42,21,0,133,137,3,44,22,0,134,137,3,46,23,0,135,137,
        3,48,24,0,136,124,1,0,0,0,136,125,1,0,0,0,136,126,1,0,0,0,136,127,
        1,0,0,0,136,128,1,0,0,0,136,129,1,0,0,0,136,130,1,0,0,0,136,131,
        1,0,0,0,136,132,1,0,0,0,136,133,1,0,0,0,136,134,1,0,0,0,136,135,
        1,0,0,0,137,19,1,0,0,0,138,139,3,14,7,0,139,142,5,43,0,0,140,141,
        5,31,0,0,141,143,3,52,26,0,142,140,1,0,0,0,142,143,1,0,0,0,143,144,
        1,0,0,0,144,145,5,38,0,0,145,21,1,0,0,0,146,147,3,16,8,0,147,150,
        5,43,0,0,148,149,5,31,0,0,149,151,3,24,12,0,150,148,1,0,0,0,150,
        151,1,0,0,0,151,152,1,0,0,0,152,153,5,38,0,0,153,23,1,0,0,0,154,
        163,5,36,0,0,155,160,3,52,26,0,156,157,5,39,0,0,157,159,3,52,26,
        0,158,156,1,0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,
        0,161,164,1,0,0,0,162,160,1,0,0,0,163,155,1,0,0,0,163,164,1,0,0,
        0,164,165,1,0,0,0,165,166,5,37,0,0,166,25,1,0,0,0,167,168,5,43,0,
        0,168,169,5,31,0,0,169,170,3,52,26,0,170,171,5,38,0,0,171,27,1,0,
        0,0,172,173,5,43,0,0,173,174,5,36,0,0,174,175,3,52,26,0,175,176,
        5,37,0,0,176,177,5,31,0,0,177,178,3,52,26,0,178,179,5,38,0,0,179,
        29,1,0,0,0,180,181,5,1,0,0,181,182,5,32,0,0,182,183,3,52,26,0,183,
        184,5,33,0,0,184,187,3,50,25,0,185,186,5,2,0,0,186,188,3,50,25,0,
        187,185,1,0,0,0,187,188,1,0,0,0,188,31,1,0,0,0,189,190,5,3,0,0,190,
        191,5,32,0,0,191,192,3,52,26,0,192,193,5,33,0,0,193,194,3,50,25,
        0,194,33,1,0,0,0,195,196,5,4,0,0,196,197,5,32,0,0,197,198,3,36,18,
        0,198,199,5,38,0,0,199,200,3,52,26,0,200,201,5,38,0,0,201,202,3,
        38,19,0,202,203,5,33,0,0,203,204,3,50,25,0,204,35,1,0,0,0,205,206,
        3,14,7,0,206,207,5,43,0,0,207,208,5,31,0,0,208,209,3,52,26,0,209,
        214,1,0,0,0,210,211,5,43,0,0,211,212,5,31,0,0,212,214,3,52,26,0,
        213,205,1,0,0,0,213,210,1,0,0,0,214,37,1,0,0,0,215,216,5,43,0,0,
        216,217,5,31,0,0,217,218,3,52,26,0,218,39,1,0,0,0,219,221,5,5,0,
        0,220,222,3,52,26,0,221,220,1,0,0,0,221,222,1,0,0,0,222,223,1,0,
        0,0,223,224,5,38,0,0,224,41,1,0,0,0,225,226,5,6,0,0,226,227,5,38,
        0,0,227,43,1,0,0,0,228,229,5,7,0,0,229,230,5,38,0,0,230,45,1,0,0,
        0,231,232,5,8,0,0,232,233,5,32,0,0,233,234,3,52,26,0,234,235,5,33,
        0,0,235,236,5,38,0,0,236,47,1,0,0,0,237,238,3,52,26,0,238,239,5,
        38,0,0,239,49,1,0,0,0,240,244,5,34,0,0,241,243,3,18,9,0,242,241,
        1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,245,1,0,0,0,245,247,
        1,0,0,0,246,244,1,0,0,0,247,248,5,35,0,0,248,51,1,0,0,0,249,250,
        6,26,-1,0,250,251,5,30,0,0,251,275,3,52,26,10,252,253,5,18,0,0,253,
        275,3,52,26,9,254,255,5,43,0,0,255,256,5,36,0,0,256,257,3,52,26,
        0,257,258,5,37,0,0,258,275,1,0,0,0,259,260,5,43,0,0,260,262,5,32,
        0,0,261,263,3,54,27,0,262,261,1,0,0,0,262,263,1,0,0,0,263,264,1,
        0,0,0,264,275,5,33,0,0,265,266,5,32,0,0,266,267,3,52,26,0,267,268,
        5,33,0,0,268,275,1,0,0,0,269,275,5,40,0,0,270,275,5,41,0,0,271,275,
        5,16,0,0,272,275,5,42,0,0,273,275,5,43,0,0,274,249,1,0,0,0,274,252,
        1,0,0,0,274,254,1,0,0,0,274,259,1,0,0,0,274,265,1,0,0,0,274,269,
        1,0,0,0,274,270,1,0,0,0,274,271,1,0,0,0,274,272,1,0,0,0,274,273,
        1,0,0,0,275,293,1,0,0,0,276,277,10,15,0,0,277,278,7,1,0,0,278,292,
        3,52,26,16,279,280,10,14,0,0,280,281,7,2,0,0,281,292,3,52,26,15,
        282,283,10,13,0,0,283,284,7,3,0,0,284,292,3,52,26,14,285,286,10,
        12,0,0,286,287,5,28,0,0,287,292,3,52,26,13,288,289,10,11,0,0,289,
        290,5,29,0,0,290,292,3,52,26,12,291,276,1,0,0,0,291,279,1,0,0,0,
        291,282,1,0,0,0,291,285,1,0,0,0,291,288,1,0,0,0,292,295,1,0,0,0,
        293,291,1,0,0,0,293,294,1,0,0,0,294,53,1,0,0,0,295,293,1,0,0,0,296,
        301,3,52,26,0,297,298,5,39,0,0,298,300,3,52,26,0,299,297,1,0,0,0,
        300,303,1,0,0,0,301,299,1,0,0,0,301,302,1,0,0,0,302,55,1,0,0,0,303,
        301,1,0,0,0,22,58,64,72,82,90,97,106,122,136,142,150,160,163,187,
        213,221,244,262,274,291,293,301
    ]

class gramatica_v3Parser ( Parser ):

    grammarFileName = "gramatica_v3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'while'", "'for'", 
                     "'return'", "'break'", "'continue'", "'print'", "'program'", 
                     "'import'", "'void'", "'int'", "'float'", "'bool'", 
                     "'string'", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'=='", "<INVALID>", "'<='", "'>='", "'<'", 
                     "'>'", "'&&'", "'||'", "'!'", "'='", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "WHILE", "FOR", "RETURN", 
                      "BREAK", "CONTINUE", "PRINT", "PROGRAM", "IMPORT", 
                      "VOID", "INT_T", "FLOAT_T", "BOOL_T", "STRING_T", 
                      "BOOL_LIT", "SUMA", "RESTA", "MULTIP", "DIV", "MOD", 
                      "EQ", "NOEQ", "MENIQ", "MAYIQ", "MENOR", "MAYOR", 
                      "AND", "OR", "NOT", "ASIGNA", "PARENA", "PARENC", 
                      "LLAVEA", "LLAVEC", "CORCHETA", "CORCHETC", "PCOMA", 
                      "COMMA", "FLOAT_LIT", "NUM", "STRING_LIT", "ID", "WS", 
                      "COMMENT", "BLOQUE_COMM" ]

    RULE_program = 0
    RULE_topLevelDecl = 1
    RULE_importDecl = 2
    RULE_funcDecl = 3
    RULE_returnType = 4
    RULE_paramList = 5
    RULE_param = 6
    RULE_t_type = 7
    RULE_arrayType = 8
    RULE_statement = 9
    RULE_varDecl = 10
    RULE_arrayDecl = 11
    RULE_arrayLiteral = 12
    RULE_assignment = 13
    RULE_arrayAssign = 14
    RULE_ifStatement = 15
    RULE_whileStatement = 16
    RULE_forStatement = 17
    RULE_forInit = 18
    RULE_forUpdate = 19
    RULE_returnStatement = 20
    RULE_breakStatement = 21
    RULE_continueStatement = 22
    RULE_printStatement = 23
    RULE_exprStatement = 24
    RULE_block = 25
    RULE_expr = 26
    RULE_argList = 27

    ruleNames =  [ "program", "topLevelDecl", "importDecl", "funcDecl", 
                   "returnType", "paramList", "param", "t_type", "arrayType", 
                   "statement", "varDecl", "arrayDecl", "arrayLiteral", 
                   "assignment", "arrayAssign", "ifStatement", "whileStatement", 
                   "forStatement", "forInit", "forUpdate", "returnStatement", 
                   "breakStatement", "continueStatement", "printStatement", 
                   "exprStatement", "block", "expr", "argList" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    WHILE=3
    FOR=4
    RETURN=5
    BREAK=6
    CONTINUE=7
    PRINT=8
    PROGRAM=9
    IMPORT=10
    VOID=11
    INT_T=12
    FLOAT_T=13
    BOOL_T=14
    STRING_T=15
    BOOL_LIT=16
    SUMA=17
    RESTA=18
    MULTIP=19
    DIV=20
    MOD=21
    EQ=22
    NOEQ=23
    MENIQ=24
    MAYIQ=25
    MENOR=26
    MAYOR=27
    AND=28
    OR=29
    NOT=30
    ASIGNA=31
    PARENA=32
    PARENC=33
    LLAVEA=34
    LLAVEC=35
    CORCHETA=36
    CORCHETC=37
    PCOMA=38
    COMMA=39
    FLOAT_LIT=40
    NUM=41
    STRING_LIT=42
    ID=43
    WS=44
    COMMENT=45
    BLOQUE_COMM=46

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
            return self.getToken(gramatica_v3Parser.PROGRAM, 0)

        def LLAVEA(self):
            return self.getToken(gramatica_v3Parser.LLAVEA, 0)

        def LLAVEC(self):
            return self.getToken(gramatica_v3Parser.LLAVEC, 0)

        def EOF(self):
            return self.getToken(gramatica_v3Parser.EOF, 0)

        def ID(self):
            return self.getToken(gramatica_v3Parser.ID, 0)

        def topLevelDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.TopLevelDeclContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.TopLevelDeclContext,i)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = gramatica_v3Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(gramatica_v3Parser.PROGRAM)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 57
                self.match(gramatica_v3Parser.ID)


            self.state = 60
            self.match(gramatica_v3Parser.LLAVEA)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.topLevelDecl()
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 16498043518458) != 0)):
                    break

            self.state = 66
            self.match(gramatica_v3Parser.LLAVEC)
            self.state = 67
            self.match(gramatica_v3Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopLevelDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_topLevelDecl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TopStatementContext(TopLevelDeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.TopLevelDeclContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(gramatica_v3Parser.StatementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopStatement" ):
                return visitor.visitTopStatement(self)
            else:
                return visitor.visitChildren(self)


    class TopFuncDeclContext(TopLevelDeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.TopLevelDeclContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcDecl(self):
            return self.getTypedRuleContext(gramatica_v3Parser.FuncDeclContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopFuncDecl" ):
                return visitor.visitTopFuncDecl(self)
            else:
                return visitor.visitChildren(self)


    class TopImportContext(TopLevelDeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.TopLevelDeclContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def importDecl(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ImportDeclContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopImport" ):
                return visitor.visitTopImport(self)
            else:
                return visitor.visitChildren(self)



    def topLevelDecl(self):

        localctx = gramatica_v3Parser.TopLevelDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_topLevelDecl)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = gramatica_v3Parser.TopFuncDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.funcDecl()
                pass

            elif la_ == 2:
                localctx = gramatica_v3Parser.TopImportContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.importDecl()
                pass

            elif la_ == 3:
                localctx = gramatica_v3Parser.TopStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(gramatica_v3Parser.IMPORT, 0)

        def ID(self):
            return self.getToken(gramatica_v3Parser.ID, 0)

        def PCOMA(self):
            return self.getToken(gramatica_v3Parser.PCOMA, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_importDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportDecl" ):
                return visitor.visitImportDecl(self)
            else:
                return visitor.visitChildren(self)




    def importDecl(self):

        localctx = gramatica_v3Parser.ImportDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_importDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(gramatica_v3Parser.IMPORT)
            self.state = 75
            self.match(gramatica_v3Parser.ID)
            self.state = 76
            self.match(gramatica_v3Parser.PCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnType(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ReturnTypeContext,0)


        def ID(self):
            return self.getToken(gramatica_v3Parser.ID, 0)

        def PARENA(self):
            return self.getToken(gramatica_v3Parser.PARENA, 0)

        def PARENC(self):
            return self.getToken(gramatica_v3Parser.PARENC, 0)

        def block(self):
            return self.getTypedRuleContext(gramatica_v3Parser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ParamListContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_funcDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = gramatica_v3Parser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.returnType()
            self.state = 79
            self.match(gramatica_v3Parser.ID)
            self.state = 80
            self.match(gramatica_v3Parser.PARENA)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0):
                self.state = 81
                self.paramList()


            self.state = 84
            self.match(gramatica_v3Parser.PARENC)
            self.state = 85
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_type(self):
            return self.getTypedRuleContext(gramatica_v3Parser.T_typeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ArrayTypeContext,0)


        def VOID(self):
            return self.getToken(gramatica_v3Parser.VOID, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_returnType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnType" ):
                return visitor.visitReturnType(self)
            else:
                return visitor.visitChildren(self)




    def returnType(self):

        localctx = gramatica_v3Parser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_returnType)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.t_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.arrayType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.match(gramatica_v3Parser.VOID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ParamContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.COMMA)
            else:
                return self.getToken(gramatica_v3Parser.COMMA, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = gramatica_v3Parser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.param()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 93
                self.match(gramatica_v3Parser.COMMA)
                self.state = 94
                self.param()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_type(self):
            return self.getTypedRuleContext(gramatica_v3Parser.T_typeContext,0)


        def ID(self):
            return self.getToken(gramatica_v3Parser.ID, 0)

        def arrayType(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = gramatica_v3Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.t_type()
                self.state = 101
                self.match(gramatica_v3Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.arrayType()
                self.state = 104
                self.match(gramatica_v3Parser.ID)
                pass


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
            return self.getToken(gramatica_v3Parser.INT_T, 0)

        def FLOAT_T(self):
            return self.getToken(gramatica_v3Parser.FLOAT_T, 0)

        def BOOL_T(self):
            return self.getToken(gramatica_v3Parser.BOOL_T, 0)

        def STRING_T(self):
            return self.getToken(gramatica_v3Parser.STRING_T, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_t_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_type" ):
                return visitor.visitT_type(self)
            else:
                return visitor.visitChildren(self)




    def t_type(self):

        localctx = gramatica_v3Parser.T_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_t_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
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


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_arrayType

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BoolArrayTypeContext(ArrayTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ArrayTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_T(self):
            return self.getToken(gramatica_v3Parser.BOOL_T, 0)
        def CORCHETA(self):
            return self.getToken(gramatica_v3Parser.CORCHETA, 0)
        def CORCHETC(self):
            return self.getToken(gramatica_v3Parser.CORCHETC, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolArrayType" ):
                return visitor.visitBoolArrayType(self)
            else:
                return visitor.visitChildren(self)


    class IntArrayTypeContext(ArrayTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ArrayTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_T(self):
            return self.getToken(gramatica_v3Parser.INT_T, 0)
        def CORCHETA(self):
            return self.getToken(gramatica_v3Parser.CORCHETA, 0)
        def CORCHETC(self):
            return self.getToken(gramatica_v3Parser.CORCHETC, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntArrayType" ):
                return visitor.visitIntArrayType(self)
            else:
                return visitor.visitChildren(self)


    class StringArrayTypeContext(ArrayTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ArrayTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_T(self):
            return self.getToken(gramatica_v3Parser.STRING_T, 0)
        def CORCHETA(self):
            return self.getToken(gramatica_v3Parser.CORCHETA, 0)
        def CORCHETC(self):
            return self.getToken(gramatica_v3Parser.CORCHETC, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringArrayType" ):
                return visitor.visitStringArrayType(self)
            else:
                return visitor.visitChildren(self)


    class FloatArrayTypeContext(ArrayTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ArrayTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_T(self):
            return self.getToken(gramatica_v3Parser.FLOAT_T, 0)
        def CORCHETA(self):
            return self.getToken(gramatica_v3Parser.CORCHETA, 0)
        def CORCHETC(self):
            return self.getToken(gramatica_v3Parser.CORCHETC, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatArrayType" ):
                return visitor.visitFloatArrayType(self)
            else:
                return visitor.visitChildren(self)



    def arrayType(self):

        localctx = gramatica_v3Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arrayType)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = gramatica_v3Parser.IntArrayTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(gramatica_v3Parser.INT_T)
                self.state = 111
                self.match(gramatica_v3Parser.CORCHETA)
                self.state = 112
                self.match(gramatica_v3Parser.CORCHETC)
                pass
            elif token in [13]:
                localctx = gramatica_v3Parser.FloatArrayTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(gramatica_v3Parser.FLOAT_T)
                self.state = 114
                self.match(gramatica_v3Parser.CORCHETA)
                self.state = 115
                self.match(gramatica_v3Parser.CORCHETC)
                pass
            elif token in [14]:
                localctx = gramatica_v3Parser.BoolArrayTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.match(gramatica_v3Parser.BOOL_T)
                self.state = 117
                self.match(gramatica_v3Parser.CORCHETA)
                self.state = 118
                self.match(gramatica_v3Parser.CORCHETC)
                pass
            elif token in [15]:
                localctx = gramatica_v3Parser.StringArrayTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 119
                self.match(gramatica_v3Parser.STRING_T)
                self.state = 120
                self.match(gramatica_v3Parser.CORCHETA)
                self.state = 121
                self.match(gramatica_v3Parser.CORCHETC)
                pass
            else:
                raise NoViableAltException(self)

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
            return self.getTypedRuleContext(gramatica_v3Parser.VarDeclContext,0)


        def arrayDecl(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ArrayDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(gramatica_v3Parser.AssignmentContext,0)


        def arrayAssign(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ArrayAssignContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(gramatica_v3Parser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(gramatica_v3Parser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ForStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ReturnStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(gramatica_v3Parser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ContinueStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(gramatica_v3Parser.PrintStatementContext,0)


        def exprStatement(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprStatementContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = gramatica_v3Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.arrayDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.arrayAssign()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.ifStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.whileStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 130
                self.forStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 131
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 132
                self.breakStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 133
                self.continueStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 134
                self.printStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 135
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
            return self.getTypedRuleContext(gramatica_v3Parser.T_typeContext,0)


        def ID(self):
            return self.getToken(gramatica_v3Parser.ID, 0)

        def PCOMA(self):
            return self.getToken(gramatica_v3Parser.PCOMA, 0)

        def ASIGNA(self):
            return self.getToken(gramatica_v3Parser.ASIGNA, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = gramatica_v3Parser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.t_type()
            self.state = 139
            self.match(gramatica_v3Parser.ID)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 140
                self.match(gramatica_v3Parser.ASIGNA)
                self.state = 141
                self.expr(0)


            self.state = 144
            self.match(gramatica_v3Parser.PCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayType(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ArrayTypeContext,0)


        def ID(self):
            return self.getToken(gramatica_v3Parser.ID, 0)

        def PCOMA(self):
            return self.getToken(gramatica_v3Parser.PCOMA, 0)

        def ASIGNA(self):
            return self.getToken(gramatica_v3Parser.ASIGNA, 0)

        def arrayLiteral(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ArrayLiteralContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_arrayDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDecl" ):
                return visitor.visitArrayDecl(self)
            else:
                return visitor.visitChildren(self)




    def arrayDecl(self):

        localctx = gramatica_v3Parser.ArrayDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.arrayType()
            self.state = 147
            self.match(gramatica_v3Parser.ID)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 148
                self.match(gramatica_v3Parser.ASIGNA)
                self.state = 149
                self.arrayLiteral()


            self.state = 152
            self.match(gramatica_v3Parser.PCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CORCHETA(self):
            return self.getToken(gramatica_v3Parser.CORCHETA, 0)

        def CORCHETC(self):
            return self.getToken(gramatica_v3Parser.CORCHETC, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.COMMA)
            else:
                return self.getToken(gramatica_v3Parser.COMMA, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_arrayLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = gramatica_v3Parser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(gramatica_v3Parser.CORCHETA)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16498043453440) != 0):
                self.state = 155
                self.expr(0)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==39:
                    self.state = 156
                    self.match(gramatica_v3Parser.COMMA)
                    self.state = 157
                    self.expr(0)
                    self.state = 162
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 165
            self.match(gramatica_v3Parser.CORCHETC)
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
            return self.getToken(gramatica_v3Parser.ID, 0)

        def ASIGNA(self):
            return self.getToken(gramatica_v3Parser.ASIGNA, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def PCOMA(self):
            return self.getToken(gramatica_v3Parser.PCOMA, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = gramatica_v3Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(gramatica_v3Parser.ID)
            self.state = 168
            self.match(gramatica_v3Parser.ASIGNA)
            self.state = 169
            self.expr(0)
            self.state = 170
            self.match(gramatica_v3Parser.PCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramatica_v3Parser.ID, 0)

        def CORCHETA(self):
            return self.getToken(gramatica_v3Parser.CORCHETA, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)


        def CORCHETC(self):
            return self.getToken(gramatica_v3Parser.CORCHETC, 0)

        def ASIGNA(self):
            return self.getToken(gramatica_v3Parser.ASIGNA, 0)

        def PCOMA(self):
            return self.getToken(gramatica_v3Parser.PCOMA, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_arrayAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAssign" ):
                return visitor.visitArrayAssign(self)
            else:
                return visitor.visitChildren(self)




    def arrayAssign(self):

        localctx = gramatica_v3Parser.ArrayAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arrayAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(gramatica_v3Parser.ID)
            self.state = 173
            self.match(gramatica_v3Parser.CORCHETA)
            self.state = 174
            self.expr(0)
            self.state = 175
            self.match(gramatica_v3Parser.CORCHETC)
            self.state = 176
            self.match(gramatica_v3Parser.ASIGNA)
            self.state = 177
            self.expr(0)
            self.state = 178
            self.match(gramatica_v3Parser.PCOMA)
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
            return self.getToken(gramatica_v3Parser.IF, 0)

        def PARENA(self):
            return self.getToken(gramatica_v3Parser.PARENA, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def PARENC(self):
            return self.getToken(gramatica_v3Parser.PARENC, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.BlockContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.BlockContext,i)


        def ELSE(self):
            return self.getToken(gramatica_v3Parser.ELSE, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = gramatica_v3Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(gramatica_v3Parser.IF)
            self.state = 181
            self.match(gramatica_v3Parser.PARENA)
            self.state = 182
            self.expr(0)
            self.state = 183
            self.match(gramatica_v3Parser.PARENC)
            self.state = 184
            self.block()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 185
                self.match(gramatica_v3Parser.ELSE)
                self.state = 186
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(gramatica_v3Parser.WHILE, 0)

        def PARENA(self):
            return self.getToken(gramatica_v3Parser.PARENA, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def PARENC(self):
            return self.getToken(gramatica_v3Parser.PARENC, 0)

        def block(self):
            return self.getTypedRuleContext(gramatica_v3Parser.BlockContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_whileStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = gramatica_v3Parser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(gramatica_v3Parser.WHILE)
            self.state = 190
            self.match(gramatica_v3Parser.PARENA)
            self.state = 191
            self.expr(0)
            self.state = 192
            self.match(gramatica_v3Parser.PARENC)
            self.state = 193
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(gramatica_v3Parser.FOR, 0)

        def PARENA(self):
            return self.getToken(gramatica_v3Parser.PARENA, 0)

        def forInit(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ForInitContext,0)


        def PCOMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.PCOMA)
            else:
                return self.getToken(gramatica_v3Parser.PCOMA, i)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ForUpdateContext,0)


        def PARENC(self):
            return self.getToken(gramatica_v3Parser.PARENC, 0)

        def block(self):
            return self.getTypedRuleContext(gramatica_v3Parser.BlockContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = gramatica_v3Parser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(gramatica_v3Parser.FOR)
            self.state = 196
            self.match(gramatica_v3Parser.PARENA)
            self.state = 197
            self.forInit()
            self.state = 198
            self.match(gramatica_v3Parser.PCOMA)
            self.state = 199
            self.expr(0)
            self.state = 200
            self.match(gramatica_v3Parser.PCOMA)
            self.state = 201
            self.forUpdate()
            self.state = 202
            self.match(gramatica_v3Parser.PARENC)
            self.state = 203
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_forInit

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForInitDeclContext(ForInitContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ForInitContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def t_type(self):
            return self.getTypedRuleContext(gramatica_v3Parser.T_typeContext,0)

        def ID(self):
            return self.getToken(gramatica_v3Parser.ID, 0)
        def ASIGNA(self):
            return self.getToken(gramatica_v3Parser.ASIGNA, 0)
        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitDecl" ):
                return visitor.visitForInitDecl(self)
            else:
                return visitor.visitChildren(self)


    class ForInitAssignContext(ForInitContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ForInitContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramatica_v3Parser.ID, 0)
        def ASIGNA(self):
            return self.getToken(gramatica_v3Parser.ASIGNA, 0)
        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitAssign" ):
                return visitor.visitForInitAssign(self)
            else:
                return visitor.visitChildren(self)



    def forInit(self):

        localctx = gramatica_v3Parser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_forInit)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 14, 15]:
                localctx = gramatica_v3Parser.ForInitDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.t_type()
                self.state = 206
                self.match(gramatica_v3Parser.ID)
                self.state = 207
                self.match(gramatica_v3Parser.ASIGNA)
                self.state = 208
                self.expr(0)
                pass
            elif token in [43]:
                localctx = gramatica_v3Parser.ForInitAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.match(gramatica_v3Parser.ID)
                self.state = 211
                self.match(gramatica_v3Parser.ASIGNA)
                self.state = 212
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramatica_v3Parser.ID, 0)

        def ASIGNA(self):
            return self.getToken(gramatica_v3Parser.ASIGNA, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_forUpdate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = gramatica_v3Parser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(gramatica_v3Parser.ID)
            self.state = 216
            self.match(gramatica_v3Parser.ASIGNA)
            self.state = 217
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(gramatica_v3Parser.RETURN, 0)

        def PCOMA(self):
            return self.getToken(gramatica_v3Parser.PCOMA, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = gramatica_v3Parser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(gramatica_v3Parser.RETURN)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16498043453440) != 0):
                self.state = 220
                self.expr(0)


            self.state = 223
            self.match(gramatica_v3Parser.PCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(gramatica_v3Parser.BREAK, 0)

        def PCOMA(self):
            return self.getToken(gramatica_v3Parser.PCOMA, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = gramatica_v3Parser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(gramatica_v3Parser.BREAK)
            self.state = 226
            self.match(gramatica_v3Parser.PCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(gramatica_v3Parser.CONTINUE, 0)

        def PCOMA(self):
            return self.getToken(gramatica_v3Parser.PCOMA, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_continueStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = gramatica_v3Parser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(gramatica_v3Parser.CONTINUE)
            self.state = 229
            self.match(gramatica_v3Parser.PCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(gramatica_v3Parser.PRINT, 0)

        def PARENA(self):
            return self.getToken(gramatica_v3Parser.PARENA, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def PARENC(self):
            return self.getToken(gramatica_v3Parser.PARENC, 0)

        def PCOMA(self):
            return self.getToken(gramatica_v3Parser.PCOMA, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_printStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = gramatica_v3Parser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(gramatica_v3Parser.PRINT)
            self.state = 232
            self.match(gramatica_v3Parser.PARENA)
            self.state = 233
            self.expr(0)
            self.state = 234
            self.match(gramatica_v3Parser.PARENC)
            self.state = 235
            self.match(gramatica_v3Parser.PCOMA)
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
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def PCOMA(self):
            return self.getToken(gramatica_v3Parser.PCOMA, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_exprStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStatement" ):
                return visitor.visitExprStatement(self)
            else:
                return visitor.visitChildren(self)




    def exprStatement(self):

        localctx = gramatica_v3Parser.ExprStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exprStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.expr(0)
            self.state = 238
            self.match(gramatica_v3Parser.PCOMA)
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

        def LLAVEA(self):
            return self.getToken(gramatica_v3Parser.LLAVEA, 0)

        def LLAVEC(self):
            return self.getToken(gramatica_v3Parser.LLAVEC, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.StatementContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.StatementContext,i)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = gramatica_v3Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(gramatica_v3Parser.LLAVEA)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16498043515386) != 0):
                self.state = 241
                self.statement()
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 247
            self.match(gramatica_v3Parser.LLAVEC)
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
            return gramatica_v3Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)

        def OR(self):
            return self.getToken(gramatica_v3Parser.OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramatica_v3Parser.ID, 0)
        def PARENA(self):
            return self.getToken(gramatica_v3Parser.PARENA, 0)
        def PARENC(self):
            return self.getToken(gramatica_v3Parser.PARENC, 0)
        def argList(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ArgListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallExpr" ):
                return visitor.visitFuncCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PARENA(self):
            return self.getToken(gramatica_v3Parser.PARENA, 0)
        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)

        def PARENC(self):
            return self.getToken(gramatica_v3Parser.PARENC, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(gramatica_v3Parser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumExpr" ):
                return visitor.visitNumExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LIT(self):
            return self.getToken(gramatica_v3Parser.STRING_LIT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class FloatExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_LIT(self):
            return self.getToken(gramatica_v3Parser.FLOAT_LIT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(gramatica_v3Parser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArrayAccessExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramatica_v3Parser.ID, 0)
        def CORCHETA(self):
            return self.getToken(gramatica_v3Parser.CORCHETA, 0)
        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)

        def CORCHETC(self):
            return self.getToken(gramatica_v3Parser.CORCHETC, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccessExpr" ):
                return visitor.visitArrayAccessExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)

        def SUMA(self):
            return self.getToken(gramatica_v3Parser.SUMA, 0)
        def RESTA(self):
            return self.getToken(gramatica_v3Parser.RESTA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RESTA(self):
            return self.getToken(gramatica_v3Parser.RESTA, 0)
        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegExpr" ):
                return visitor.visitNegExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)

        def MULTIP(self):
            return self.getToken(gramatica_v3Parser.MULTIP, 0)
        def DIV(self):
            return self.getToken(gramatica_v3Parser.DIV, 0)
        def MOD(self):
            return self.getToken(gramatica_v3Parser.MOD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class BoolExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_LIT(self):
            return self.getToken(gramatica_v3Parser.BOOL_LIT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)

        def EQ(self):
            return self.getToken(gramatica_v3Parser.EQ, 0)
        def NOEQ(self):
            return self.getToken(gramatica_v3Parser.NOEQ, 0)
        def MENOR(self):
            return self.getToken(gramatica_v3Parser.MENOR, 0)
        def MAYOR(self):
            return self.getToken(gramatica_v3Parser.MAYOR, 0)
        def MENIQ(self):
            return self.getToken(gramatica_v3Parser.MENIQ, 0)
        def MAYIQ(self):
            return self.getToken(gramatica_v3Parser.MAYIQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramatica_v3Parser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)

        def AND(self):
            return self.getToken(gramatica_v3Parser.AND, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramatica_v3Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = gramatica_v3Parser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 250
                self.match(gramatica_v3Parser.NOT)
                self.state = 251
                self.expr(10)
                pass

            elif la_ == 2:
                localctx = gramatica_v3Parser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 252
                self.match(gramatica_v3Parser.RESTA)
                self.state = 253
                self.expr(9)
                pass

            elif la_ == 3:
                localctx = gramatica_v3Parser.ArrayAccessExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 254
                self.match(gramatica_v3Parser.ID)
                self.state = 255
                self.match(gramatica_v3Parser.CORCHETA)
                self.state = 256
                self.expr(0)
                self.state = 257
                self.match(gramatica_v3Parser.CORCHETC)
                pass

            elif la_ == 4:
                localctx = gramatica_v3Parser.FuncCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 259
                self.match(gramatica_v3Parser.ID)
                self.state = 260
                self.match(gramatica_v3Parser.PARENA)
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16498043453440) != 0):
                    self.state = 261
                    self.argList()


                self.state = 264
                self.match(gramatica_v3Parser.PARENC)
                pass

            elif la_ == 5:
                localctx = gramatica_v3Parser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 265
                self.match(gramatica_v3Parser.PARENA)
                self.state = 266
                self.expr(0)
                self.state = 267
                self.match(gramatica_v3Parser.PARENC)
                pass

            elif la_ == 6:
                localctx = gramatica_v3Parser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 269
                self.match(gramatica_v3Parser.FLOAT_LIT)
                pass

            elif la_ == 7:
                localctx = gramatica_v3Parser.NumExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 270
                self.match(gramatica_v3Parser.NUM)
                pass

            elif la_ == 8:
                localctx = gramatica_v3Parser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 271
                self.match(gramatica_v3Parser.BOOL_LIT)
                pass

            elif la_ == 9:
                localctx = gramatica_v3Parser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 272
                self.match(gramatica_v3Parser.STRING_LIT)
                pass

            elif la_ == 10:
                localctx = gramatica_v3Parser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 273
                self.match(gramatica_v3Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 291
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = gramatica_v3Parser.MulExprContext(self, gramatica_v3Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 276
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 277
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 278
                        self.expr(16)
                        pass

                    elif la_ == 2:
                        localctx = gramatica_v3Parser.AddExprContext(self, gramatica_v3Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 279
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 280
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 281
                        self.expr(15)
                        pass

                    elif la_ == 3:
                        localctx = gramatica_v3Parser.RelExprContext(self, gramatica_v3Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 282
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 283
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 284
                        self.expr(14)
                        pass

                    elif la_ == 4:
                        localctx = gramatica_v3Parser.AndExprContext(self, gramatica_v3Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 285
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 286
                        self.match(gramatica_v3Parser.AND)
                        self.state = 287
                        self.expr(13)
                        pass

                    elif la_ == 5:
                        localctx = gramatica_v3Parser.OrExprContext(self, gramatica_v3Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 288
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 289
                        self.match(gramatica_v3Parser.OR)
                        self.state = 290
                        self.expr(12)
                        pass

             
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.COMMA)
            else:
                return self.getToken(gramatica_v3Parser.COMMA, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_argList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = gramatica_v3Parser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.expr(0)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 297
                self.match(gramatica_v3Parser.COMMA)
                self.state = 298
                self.expr(0)
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         




