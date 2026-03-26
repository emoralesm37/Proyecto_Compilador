grammar Expresiones;

// ============================================================
// REGLA INICIAL
// ============================================================
program
    : PROGRAM LLAVEA topLevelDecl+ LLAVEC EOF
    ;

// Declaraciones de nivel superior: funciones o sentencias
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
    : type          // int, float, bool, string
    | VOID          // void
    ;

paramList
    : param (COMMA param)*
    ;

param
    : type ID
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

// Declaración con inicialización opcional: int x; o int x = 10;
varDecl
    : type ID (ASIGNA expr)? PCOMA
    ;

// Asignación: x = expr;
assignment
    : ID ASIGNA expr PCOMA
    ;

// Condicional
ifStatement
    : IF PARENA expr PARENC block (ELSE block)?
    ;

// Ciclo while
whileStatement
    : WHILE PARENA expr PARENC block
    ;

// Ciclo for: for (init; condición; actualización)
forStatement
    : FOR PARENA forInit PCOMA expr PCOMA forUpdate PARENC block
    ;

forInit
    : type ID ASIGNA expr       # forInitDecl
    | ID ASIGNA expr            # forInitAssign
    ;

forUpdate
    : ID ASIGNA expr
    ;

// Retorno de función
returnStatement
    : RETURN expr? PCOMA
    ;

// Impresión
printStatement
    : PRINT PARENA expr PARENC PCOMA
    ;

// Expresión como sentencia
exprStatement
    : expr PCOMA
    ;

// Bloque de código
block
    : LLAVEA statement* LLAVEC
    ;

// Tipos de variables
type
    : INT_T
    | FLOAT_T
    | BOOL_T
    | STRING_T
    ;

// ============================================================
// EXPRESIONES — precedencia de mayor a menor (ANTLR4: primero = más alta)
// ============================================================
expr
    // Nivel 6 — Multiplicación, División, Módulo (mayor precedencia binaria)
    : expr (MULTIP | DIV | MOD) expr                         # mulExpr

    // Nivel 5 — Suma y Resta
    | expr (SUMA | RESTA) expr                              # addExpr

    // Nivel 4 — Operadores relacionales
    | expr (EQ | NOEQ | MENOR | MAYOR | MENIQ | MAYIQ) expr           # relExpr

    // Nivel 3 — AND lógico
    | expr AND expr                                         # andExpr

    // Nivel 2 — OR lógico
    | expr OR expr                                          # orExpr

    // Unarios — alta precedencia
    | NOT expr                                              # notExpr
    | RESTA expr                                            # negExpr

    // Llamada a función: factorial(n)
    | ID PARENA argList? PARENC                             # funcCallExpr

    // Agrupación
    | PARENA expr PARENC                                    # parenExpr

    // Literales y variables (hojas del árbol)
    | FLOAT_LIT                                             # floatExpr
    | NUM                                                   # numExpr
    | BOOL_LIT                                              # boolExpr
    | STRING_LIT                                            # stringExpr
    | ID                                                    # idExpr
    ;

argList
    : expr (COMMA expr)*
    ;

// ============================================================
// TOKENS — Palabras reservadas
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

// ============================================================
// TOKENS — Operadores
// ============================================================
SUMA    : '+'  ;
RESTA   : '-'  ;
MULTIP  : '*'  ;
DIV     : '/'  ;
MOD     : '%'  ;

EQ      : '==' ;
NOEQ    : '!=' | '<>' ;
MENIQ   : '<=' ;
MAYIQ   : '>=' ;
MENOR   : '<'  ;
MAYOR   : '>'  ;

AND     : '&&' ;
OR      : '||' ;
NOT     : '!'  ;

// ============================================================
// TOKENS — Símbolos
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
// IGNORAR
// ============================================================
WS            : [ \t\r\n]+   -> skip ;
COMMENT       : '//' ~[\r\n]* -> skip ;
BLOQUE_COMM : '/*' .*? '*/' -> skip ;