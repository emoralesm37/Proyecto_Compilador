grammar gramatica_v3;

// ============================================================
// REGLA INICIAL
// ============================================================
program
    : PROGRAM ID? LLAVEA topLevelDecl+ LLAVEC EOF
    ;

topLevelDecl
    : funcDecl      # topFuncDecl
    | importDecl    # topImport
    | statement     # topStatement
    ;

// ============================================================
// IMPORTS SIMPLES
// ============================================================
importDecl
    : IMPORT ID PCOMA
    ;

// ============================================================
// DECLARACIÓN DE FUNCIONES
// ============================================================
funcDecl
    : returnType ID PARENA paramList? PARENC block
    ;

returnType
    : t_type
    | arrayType
    | VOID
    ;

paramList
    : param (COMMA param)*
    ;

param
    : t_type ID
    | arrayType ID
    ;

// ============================================================
// TIPOS (escalares y arreglos)
// ============================================================
t_type
    : INT_T
    | FLOAT_T
    | BOOL_T
    | STRING_T
    ;

arrayType
    : INT_T    CORCHETA CORCHETC    # intArrayType
    | FLOAT_T  CORCHETA CORCHETC    # floatArrayType
    | BOOL_T   CORCHETA CORCHETC    # boolArrayType
    | STRING_T CORCHETA CORCHETC    # stringArrayType
    ;

// ============================================================
// SENTENCIAS
// ============================================================
statement
    : varDecl
    | arrayDecl
    | assignment
    | arrayAssign
    | ifStatement
    | whileStatement
    | forStatement
    | returnStatement
    | breakStatement
    | continueStatement
    | printStatement
    | exprStatement
    ;

// Declaración de variable escalar: int x = 5;
varDecl
    : t_type ID (ASIGNA expr)? PCOMA
    ;

// Declaración de arreglo: int[] nums = [1, 2, 3];
arrayDecl
    : arrayType ID (ASIGNA arrayLiteral)? PCOMA
    ;

// Literal de arreglo: [1, 2, 3]
arrayLiteral
    : CORCHETA (expr (COMMA expr)*)? CORCHETC
    ;

// Asignación escalar: x = expr;
assignment
    : ID ASIGNA expr PCOMA
    ;

// Asignación a elemento de arreglo: nums[i] = expr;
arrayAssign
    : ID CORCHETA expr CORCHETC ASIGNA expr PCOMA
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
    : t_type ID ASIGNA expr     # forInitDecl
    | ID ASIGNA expr            # forInitAssign
    ;

forUpdate
    : ID ASIGNA expr
    ;

returnStatement
    : RETURN expr? PCOMA
    ;

// Break dentro de ciclos
breakStatement
    : BREAK PCOMA
    ;

// Continue dentro de ciclos
continueStatement
    : CONTINUE PCOMA
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

// ============================================================
// EXPRESIONES
// ============================================================
expr
    : expr (MULTIP | DIV | MOD) expr                                    # mulExpr
    | expr (SUMA | RESTA) expr                                          # addExpr
    | expr (EQ | NOEQ | MENOR | MAYOR | MENIQ | MAYIQ) expr            # relExpr
    | expr AND expr                                                     # andExpr
    | expr OR expr                                                      # orExpr
    | NOT expr                                                          # notExpr
    | RESTA expr                                                        # negExpr
    | ID CORCHETA expr CORCHETC                                         # arrayAccessExpr
    | ID PARENA argList? PARENC                                         # funcCallExpr
    | PARENA expr PARENC                                                # parenExpr
    | FLOAT_LIT                                                         # floatExpr
    | NUM                                                               # numExpr
    | BOOL_LIT                                                          # boolExpr
    | STRING_LIT                                                        # stringExpr
    | ID                                                                # idExpr
    ;

argList
    : expr (COMMA expr)*
    ;

// ============================================================
// TOKENS — Palabras reservadas
// ============================================================
IF       : 'if'       ;
ELSE     : 'else'     ;
WHILE    : 'while'    ;
FOR      : 'for'      ;
RETURN   : 'return'   ;
BREAK    : 'break'    ;
CONTINUE : 'continue' ;
PRINT    : 'print'    ;
PROGRAM  : 'program'  ;
IMPORT   : 'import'   ;
VOID     : 'void'     ;
INT_T    : 'int'      ;
FLOAT_T  : 'float'    ;
BOOL_T   : 'bool'     ;
STRING_T : 'string'   ;
BOOL_LIT : 'true' | 'false' ;

// ============================================================
// TOKENS — Operadores
// ============================================================
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

// ============================================================
// TOKENS — Delimitadores y puntuación
// ============================================================
ASIGNA   : '='  ;
PARENA   : '('  ;
PARENC   : ')'  ;
LLAVEA   : '{'  ;
LLAVEC   : '}'  ;
CORCHETA : '['  ;
CORCHETC : ']'  ;
PCOMA    : ';'  ;
COMMA    : ','  ;

// ============================================================
// TOKENS — Literales
// ============================================================
FLOAT_LIT  : [0-9]+ '.' [0-9]+ ;
NUM        : [0-9]+             ;
STRING_LIT : '"' (~["\r\n])* '"' ;
ID         : [a-zA-Z_][a-zA-Z0-9_]* ;

// ============================================================
// TOKENS — Ignorados
// ============================================================
WS          : [ \t\r\n]+    -> skip ;
COMMENT     : '//' ~[\r\n]* -> skip ;
BLOQUE_COMM : '/*' .*? '*/' -> skip ;