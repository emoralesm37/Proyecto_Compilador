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
    | expr (EQ | NOEQ | MENOR | MAYOR | MENIQ | MAYIQ) expr             # relExpr
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
IF       : 'if'       ;                                                #control_condicional
ELSE     : 'else'     ;                                                #control_alternativa
WHILE    : 'while'    ;                                                #control_iterativo
FOR      : 'for'      ;                                                #control_iterativo
RETURN   : 'return'   ;                                                #transferencia_control
BREAK    : 'break'    ;                                                #transferencia_control
CONTINUE : 'continue' ;                                                #transferencia_control
PRINT    : 'print'    ;                                                #salida_datos
PROGRAM  : 'program'  ;                                                #estructura_programa
IMPORT   : 'import'   ;                                                #modularidad
VOID     : 'void'     ;                                                #tipo_dato
INT_T    : 'int'      ;                                                #tipo_dato
FLOAT_T  : 'float'    ;                                                #tipo_dato
BOOL_T   : 'bool'     ;                                                #tipo_dato
STRING_T : 'string'   ;                                                #tipo_dato
BOOL_LIT : 'true' | 'false' ;                                          #tipo_dato

// ============================================================
// TOKENS — Operadores
// ============================================================
SUMA     : '+'  ;                                                      #opAritmetico_suma
RESTA    : '-'  ;                                                      #opAritmetico_resta
MULTIP   : '*'  ;                                                      #opAritmetico_multiplicacion
DIV      : '/'  ;                                                      #opAritmetico_division
MOD      : '%'  ;                                                      #opAritmetico_modulo

EQ       : '==' ;                                                      #opRelacional_igual
NOEQ     : '!=' | '<>' ;                                               #opRelacional_diferente
MENIQ    : '<=' ;                                                      #opRelacional_menorigual
MAYIQ    : '>=' ;                                                      #opRelacional_mayorigual
MENOR    : '<'  ;                                                      #opRelacional_menor
MAYOR    : '>'  ;                                                      #opRelacional_mayor

AND      : '&&' ;                                                      #opLogico_and
OR       : '||' ;                                                      #opLogico_or
NOT      : '!'  ;                                                      #opLogico_not

// ============================================================
// TOKENS — Delimitadores y puntuación
// ============================================================
ASIGNA   : '='  ;                                                      #asignacion
PARENA   : '('  ;                                                      #parentesis_abre
PARENC   : ')'  ;                                                      #parentesis_cierra
LLAVEA   : '{'  ;                                                      #llave_abre
LLAVEC   : '}'  ;                                                      #llave_cierra
CORCHETA : '['  ;                                                      #corchete_abre
CORCHETC : ']'  ;                                                      #corchete_cierra
PCOMA    : ';'  ;                                                      #fin_sentencia
COMMA    : ','  ;                                                      #separador

// ============================================================
// TOKENS — Literales
// ============================================================
FLOAT_LIT  : [0-9]+ '.' [0-9]+ ;                                       #literal_float
NUM        : [0-9]+             ;                                      #literal_entero
STRING_LIT : '"' (~["\r\n])* '"' ;                                     #literal_string
ID         : [a-zA-Z_][a-zA-Z0-9_]* ;                                  #identificador

// ============================================================
// TOKENS — Ignorados
// ============================================================
WS          : [ \t\r\n]+    -> skip ;                                  #espacios
COMMENT     : '//' ~[\r\n]* -> skip ;                                  #comentario_linea
BLOQUE_COMM : '/*' .*? '*/' -> skip ;                                  #comentario_bloque
