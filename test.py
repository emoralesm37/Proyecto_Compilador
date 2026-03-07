# ================================================================
# el archivo se llama interprete.py
# Punto de entrada del intérprete para Expresiones
# Uso: python3 test.py <entrada>
# ================================================================

import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from ExpresionesLexer   import ExpresionesLexer
from ExpresionesParser  import ExpresionesParser
from ExpresionesVisitor  import ExpresionesVisitor


# ============================================================
# Listener personalizado para capturar errores de ANTLR4
# ============================================================
class MiErrorListener(ErrorListener):

    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error = f"  X Línea {line}, columna {column}: {msg}"
        self.errores.append(error)
        print(error)


# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================
def main(entrada: str):

    print(f"\n{'─' * 50}")
    print(f"  Expresiones Intérprete")
    print(f"  Archivo: {entrada}")
    print(f"{'─' * 50}\n")

    # ----------------------------------------------------------
    # 1. Leer el archivo de entrada
    # ----------------------------------------------------------
    try:
        input_stream = FileStream(entrada, encoding='utf-8')
    except FileNotFoundError:
        print(f"X No se encontró el archivo: '{entrada}'")
        sys.exit(1)

    # ----------------------------------------------------------
    # 2. ANÁLISIS LÉXICO
    # ----------------------------------------------------------
    lexer          = ExpresionesLexer(input_stream)
    error_listener = MiErrorListener()

    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    stream = CommonTokenStream(lexer)
    stream.fill()  # Forzar el análisis léxico completo

    if error_listener.errores:
        print(f"\n ALTO Se encontraron {len(error_listener.errores)} error(es) LÉXICOS.")
        print("ALTO Ejecución abortada.\n")
        sys.exit(1)

    print("OK Análisis léxico completado sin errores.")

    # ----------------------------------------------------------
    # 3. ANÁLISIS SINTÁCTICO
    # ----------------------------------------------------------
    parser = ExpresionesParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()  # Regla inicial de la gramática

    if error_listener.errores:
        print(f"\n X Se encontraron {len(error_listener.errores)} error(es) SINTÁCTICOS.")
        print("X Ejecución abortada.\n")
        sys.exit(1)

    print("OK Análisis sintáctico completado sin errores.")

    # Opcional: imprimir el árbol de parseo
    print(f"\n Árbol de parseo:")
    print(f"   {tree.toStringTree(recog=parser)}\n")

    # ----------------------------------------------------------
    # 4. EVALUACIÓN CON VISITOR
    # ----------------------------------------------------------
    print("─" * 50)
    try:
        visitor = ExpresionesVisitor()
        visitor.visit(tree)
        print(f"\n{'─' * 50}")
        print("OK Programa ejecutado exitosamente.")
        print(f"{'─' * 50}\n")

    except Exception as e:
        print(f"\n{e}")
        print("X Ejecución abortada por error semántico.\n")
        sys.exit(1)


# ============================================================
# ENTRADA DEL SCRIPT
# ============================================================
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\nUso:     python3 test.py <entrada>")
        print("Ejemplo: python3 test.py entrada.txt\n")
        sys.exit(1)

    main(sys.argv[1])