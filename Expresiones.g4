grammar Expresiones;

// ============================================================
// REGLA INICIAL DEL PROGRAMA
// ============================================================
program
    : PROGRAM name+ LBRACE statement* RBRACE EOF
    ;

name
    :ID 
    ;
// ============================================================
// SENTENCIAS (statements)
// ============================================================
statement
    : varDecl           // int x;
    | assignment        // x = 10;
    | ifStatement       // if (...) { } else { }
    | exprStatement     // expresión suelta, ej: x + 2;
    ;

// Declaración de variable: int x;
varDecl
    : type ID SEMI
    ;

// Asignación: x = expr;
assignment
    : ID ASSIGN expr SEMI
    ;

// Expresión como sentencia: (x + y);
exprStatement
    : expr SEMI
    ;

// Condicional: if (expr) bloque [else bloque]
ifStatement
    : IF LPAREN expr RPAREN block (ELSE block)?
    ;

// Bloque de código delimitado por llaves
block
    : LBRACE statement* RBRACE
    ;

// Tipos de datos soportados
type
    : INT_T
    | FLOAT_T
    | BOOL_T
    | STRING_T
    ;

// ============================================================
// EXPRESIONES — con precedencia correcta (mayor a menor)
// ============================================================
expr
    // Nivel 9 — Multiplicación y División
    : expr (TIMES | DIV) expr                           # mulExpr

    // Nivel 8 — Suma y Resta
    | expr (PLUS | MINUS) expr                          # addExpr

    // Nivel 7 — Operadores relacionales
    | expr (EQ | NEQ | LT | GT | LEQ | GEQ) expr       # relExpr

    // Nivel 6 — AND lógico
    | expr AND expr                                     # andExpr

    // Nivel 5 — OR lógico (menor precedencia)
    | expr OR expr                                      # orExpr

    // Nivel 4 — NOT lógico (unario)
    | NOT expr                                          # notExpr

    // Nivel 3 — Negación aritmética (unario)
    | MINUS expr                                        # negExpr

    // Nivel 2 — Agrupación con paréntesis
    | LPAREN expr RPAREN                                # parenExpr

    // Nivel 1 — Literales y variables (mayor precedencia)
    | FLOAT_LIT                                         # floatExpr
    | NUM                                               # numExpr
    | BOOL_LIT                                          # boolExpr
    | ID                                                # idExpr
    ;

// ============================================================
// TOKENS — Palabras reservadas
// ============================================================
IF       : 'if'      ;
ELSE     : 'else'    ;
PROGRAM  : 'program' ;
INT_T    : 'int'     ;
FLOAT_T  : 'float'   ;
BOOL_T   : 'bool'    ;
STRING_T : 'string'  ;
BOOL_LIT : 'true' | 'false' ;

// ============================================================
// TOKENS — Operadores aritméticos
// ============================================================
PLUS    : '+'  ;
MINUS   : '-'  ;
TIMES   : '*'  ;
DIV     : '/'  ;

// ============================================================
// TOKENS — Operadores relacionales
// IMPORTANTE: definir tokens más largos ANTES que los cortos
// Ej: '<=' antes que '<', '==' antes que '='
// ============================================================
EQ      : '==' ;
NEQ     : '!=' | '<>' ;
LEQ     : '<=' ;
GEQ     : '>=' ;
LT      : '<'  ;
GT      : '>'  ;

// ============================================================
// TOKENS — Operadores lógicos
// ============================================================
AND     : '&&' ;
OR      : '||' ;
NOT     : '!'  ;

// ============================================================
// TOKENS — Símbolos de agrupación y puntuación
// ============================================================
ASSIGN   : '='  ;       // Operador de asignación
LPAREN   : '('  ;
RPAREN   : ')'  ;
LBRACE   : '{'  ;
RBRACE   : '}'  ;
LBRACKET : '['  ;
RBRACKET : ']'  ;
SEMI     : ';'  ;

// ============================================================
// TOKENS — Literales numéricos e identificadores
// IMPORTANTE: FLOAT_LIT antes que NUM para que [0-9]+.[0-9]+
// no sea parseado como dos enteros
// ============================================================
FLOAT_LIT : [0-9]+ '.' [0-9]+ ;
NUM       : [0-9]+             ;
ID        : [a-zA-Z_][a-zA-Z0-9_]* ;

// ============================================================
// IGNORAR espacios en blanco y comentarios de línea
// ============================================================
WS      : [ \t\r\n]+  -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;