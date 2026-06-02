grammar gramatica_v4;

// ============================================================
// REGLA INICIAL
// ============================================================
program
    : PROGRAM ID? LLAVEA topLevelDecl+ LLAVEC EOF
    ;

topLevelDecl
    : funcDecl      # topFuncDecl
    | importDecl    # topImport
    | structDecl    # topStructDecl
    | statement     # topStatement
    ;

// ============================================================
// IMPORTS SIMPLES
// ============================================================
importDecl
    : IMPORT ID PCOMA
    ;

// ============================================================
// DECLARACIÓN DE STRUCTS (novedad v4)
// Los structs se definen a nivel global, antes de usarse.
// Ejemplo: struct Punto { int x; int y; }
// ============================================================
structDecl
    : STRUCT ID LLAVEA structField+ LLAVEC PCOMA
    ;

structField
    : t_type ID PCOMA
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
// TIPOS — Escalares, arreglos (v3) y structs (v4)
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
    | structVarDecl
    | assignment
    | fieldAssign
    | arrayAssign
    | ifStatement
    | whileStatement
    | forStatement
    | switchStatement
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

// Declaración de variable struct: Punto p;
// El tipo es un ID (nombre del struct definido por el usuario)
structVarDecl
    : ID ID PCOMA
    ;

// Literal de arreglo: [1, 2, 3]
arrayLiteral
    : CORCHETA (expr (COMMA expr)*)? CORCHETC
    ;

// Asignación escalar: x = expr;
assignment
    : ID ASIGNA expr PCOMA
    ;

// Asignación a campo de struct: p.x = 10;
fieldAssign
    : ID PUNTO ID ASIGNA expr PCOMA
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

// Switch / Case con default (novedad v4)
// Ejemplo: switch(x) { case 1: print(x); break; default: print(0); }
switchStatement
    : SWITCH PARENA expr PARENC LLAVEA caseClause* defaultClause? LLAVEC
    ;

caseClause
    : CASE expr DOSPUNTOS statement*
    ;

defaultClause
    : DEFAULT DOSPUNTOS statement*
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

breakStatement
    : BREAK PCOMA
    ;

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
// Orden: MENOR precedencia arriba → MAYOR precedencia abajo
// Novedades v4: ternaryExpr, castExpr, fieldAccessExpr
// ============================================================
expr
    // Operador ternario (novedad v4) — menor precedencia, derecho-asociativo
    // Ejemplo: x > 0 ? x : -x
    : <assoc=right> expr INTERROGA expr DOSPUNTOS expr                  # ternaryExpr

    // Operadores lógicos
    | expr OR  expr                                                     # orExpr
    | expr AND expr                                                     # andExpr

    // Relacionales y de igualdad
    | expr (EQ | NOEQ | MENOR | MAYOR | MENIQ | MAYIQ) expr            # relExpr

    // Aritméticos
    | expr (SUMA | RESTA) expr                                          # addExpr
    | expr (MULTIP | DIV | MOD) expr                                    # mulExpr

    // Unarios
    | NOT   expr                                                        # notExpr
    | RESTA expr                                                        # negExpr

    // Casting explícito de tipos (novedad v4)
    // Ejemplo: (float) miVar  o  (int) 3.14
    | PARENA t_type PARENC expr                                         # castExpr

    // Acceso a arreglo: nums[i]
    | ID CORCHETA expr CORCHETC                                         # arrayAccessExpr

    // Acceso a campo de struct (novedad v4): p.x
    | ID PUNTO ID                                                       # fieldAccessExpr

    // Llamada a función: factorial(n)
    | ID PARENA argList? PARENC                                         # funcCallExpr

    // Expresión entre paréntesis: (expr)
    | PARENA expr PARENC                                                # parenExpr

    // Literales y referencias
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
SWITCH   : 'switch'   ;   // novedad v4
CASE     : 'case'     ;   // novedad v4
DEFAULT  : 'default'  ;   // novedad v4
STRUCT   : 'struct'   ;   // novedad v4
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
// TOKENS — Operadores aritméticos
// ============================================================
SUMA     : '+'  ;
RESTA    : '-'  ;
MULTIP   : '*'  ;
DIV      : '/'  ;
MOD      : '%'  ;

// ============================================================
// TOKENS — Operadores relacionales y lógicos
// ============================================================
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
ASIGNA    : '='  ;
INTERROGA : '?'  ;   // novedad v4 — operador ternario
DOSPUNTOS : ':'  ;   // novedad v4 — switch/case y ternario
PUNTO     : '.'  ;   // novedad v4 — acceso a campos de struct
PARENA    : '('  ;
PARENC    : ')'  ;
LLAVEA    : '{'  ;
LLAVEC    : '}'  ;
CORCHETA  : '['  ;
CORCHETC  : ']'  ;
PCOMA     : ';'  ;
COMMA     : ','  ;

// ============================================================
// TOKENS — Literales
// ============================================================
FLOAT_LIT  : [0-9]+ '.' [0-9]+ ;   // debe ir ANTES que PUNTO
NUM        : [0-9]+             ;
STRING_LIT : '"' (~["\r\n])* '"' ;
ID         : [a-zA-Z_][a-zA-Z0-9_]* ;

// ============================================================
// TOKENS — Ignorados
// ============================================================
WS          : [ \t\r\n]+    -> skip ;
COMMENT     : '//' ~[\r\n]* -> skip ;
BLOQUE_COMM : '/*' .*? '*/' -> skip ;