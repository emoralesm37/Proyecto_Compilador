grammar Expresiones;

// ============================================================
// REGLA INICIAL
// ============================================================
program
    : PROGRAM ID? LLAVEA topLevelDecl+ LLAVEC EOF
    ;

topLevelDecl
    : funcDecl      # topFuncDecl
    | statement     # topStatement
    ;

// ============================================================
// DECLARACIÓN DE FUNCIONES
// ============================================================
funcDecl
    : returnType ID PARENA paramList? PARENC block
    ;

returnType
    : t_type          
    | VOID          
    ;

paramList
    : param (COMMA param)*
    ;

param
    : t_type ID       
    ;

// ============================================================
// SENTENCIAS
// ============================================================
statement
    : varDecl
    | assignment
    | ifStatement
    | whileStatement
    | forStatement
    | returnStatement
    | printStatement
    | exprStatement
    ;

varDecl
    : t_type ID (ASIGNA expr)? PCOMA  
    ;

assignment
    : ID ASIGNA expr PCOMA
    ;

ifStatement
    : IF PARENA expr PARENC block (ELSE block)?
    ;

whileStatement
    : WHILE PARENA expr PARENC block
    ;

forStatement
    : FOR PARENA forInit PCOMA expr PCOMA forUpdate PARENC block
    ;

forInit
    : t_type ID ASIGNA expr       # forInitDecl  
    | ID ASIGNA expr            # forInitAssign
    ;

forUpdate
    : ID ASIGNA expr
    ;

returnStatement
    : RETURN expr? PCOMA
    ;

printStatement
    : PRINT PARENA expr PARENC PCOMA
    ;

exprStatement
    : expr PCOMA
    ;

block
    : LLAVEA statement* LLAVEC
    ;

// REGLA RENOMBRADA PARA EVITAR CONFLICTO
t_type
    : INT_T
    | FLOAT_T
    | BOOL_T
    | STRING_T
    ;

// ============================================================
// EXPRESIONES
// ============================================================
expr
    : expr (MULTIP | DIV | MOD) expr                                # mulExpr
    | expr (SUMA | RESTA) expr                                      # addExpr
    | expr (EQ | NOEQ | MENOR | MAYOR | MENIQ | MAYIQ) expr           # relExpr
    | expr AND expr                                                 # andExpr
    | expr OR expr                                                  # orExpr
    | NOT expr                                                      # notExpr
    | RESTA expr                                                    # negExpr
    | ID PARENA argList? PARENC                                     # funcCallExpr
    | PARENA expr PARENC                                            # parenExpr
    | FLOAT_LIT                                                     # floatExpr
    | NUM                                                           # numExpr
    | BOOL_LIT                                                      # boolExpr
    | STRING_LIT                                                    # stringExpr
    | ID                                                            # idExpr
    ;

argList
    : expr (COMMA expr)*
    ;

// ============================================================
// TOKENS
// ============================================================
IF       : 'if'      ;
ELSE     : 'else'    ;
WHILE    : 'while'   ;
FOR      : 'for'     ;
RETURN   : 'return'  ;
PRINT    : 'print'   ;
PROGRAM  : 'program' ;
VOID     : 'void'    ;
INT_T    : 'int'     ;
FLOAT_T  : 'float'   ;
BOOL_T   : 'bool'    ;
STRING_T : 'string'  ;
BOOL_LIT : 'true' | 'false' ;

SUMA     : '+'  ;
RESTA    : '-'  ;
MULTIP   : '*'  ;
DIV      : '/'  ;
MOD      : '%'  ;

EQ       : '==' ;
NOEQ     : '!=' | '<>' ;
MENIQ    : '<=' ;
MAYIQ    : '>=' ;
MENOR    : '<'  ;
MAYOR    : '>'  ;

AND      : '&&' ;
OR       : '||' ;
NOT      : '!'  ;

ASIGNA   : '='  ;
PARENA   : '('  ;
PARENC   : ')'  ;
LLAVEA   : '{'  ;
LLAVEC   : '}'  ;
CORCHETA : '['  ;
CORCHETC : ']'  ;
PCOMA    : ';'  ;
COMMA    : ','  ;

FLOAT_LIT  : [0-9]+ '.' [0-9]+ ;
NUM        : [0-9]+             ;
STRING_LIT : '"' (~["\r\n])* '"' ;
ID         : [a-zA-Z_][a-zA-Z0-9_]* ;

WS          : [ \t\r\n]+   -> skip ;
COMMENT       : '//' ~[\r\n]* -> skip ;
BLOQUE_COMM : '/*' .*? '*/' -> skip ;