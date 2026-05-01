# ================================================================
# pipeline.py
# Orquestador principal del compilador — Proyecto 2
# Fases: Léxico → Sintáctico → Semántico → Intérprete
# ================================================================

import sys
from antlr4 import *

from ExpresionesLexer    import ExpresionesLexer
from ExpresionesParser   import ExpresionesParser
from errores_personalizados       import LexicoErrorListener, SintacticoErrorListener
from semantic_visitor    import SemanticVisitor
from interpreter_visitor import InterpreterVisitor


def separador(char="─", ancho=55):
    print(char * ancho)


def titulo(texto, char="═"):
    separador(char)
    print(f"  {texto}")
    separador(char)


def main(archivo: str):
    titulo(f"Pipeline de Compilación")
    print(f"  Archivo : {archivo}")
    print(f"  Fases   : Léxico → Sintáctico → Semántico → Intérprete")
    separador("═")
    print()

    # ──────────────────────────────────────────────────────────
    # FASE 1 — Leer archivo fuente
    # ──────────────────────────────────────────────────────────
    try:
        input_stream = FileStream(archivo, encoding='utf-8')
    except FileNotFoundError:
        print(f" X No se encontró el archivo: '{archivo}'")
        sys.exit(1)

    # ──────────────────────────────────────────────────────────
    # FASE 2 — ANÁLISIS LÉXICO (Scanner)
    # ──────────────────────────────────────────────────────────
    print(" Fase 1 — Análisis Léxico (Scanner)")

    lexer        = ExpresionesLexer(input_stream)
    err_lexico   = LexicoErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(err_lexico)

    stream = CommonTokenStream(lexer)
    stream.fill()

    if err_lexico.hay_errores():
        print(f"  X  {len(err_lexico.errores)} error(es) léxico(s):\n")
        for e in err_lexico.errores:
            print(f"      {e}")
        print("\n ALTO Pipeline detenido — fase léxica.\n")
        sys.exit(1)

    print(" Sin errores léxicos.\n")

    # ──────────────────────────────────────────────────────────
    # FASE 3 — ANÁLISIS SINTÁCTICO (Parser)
    # ──────────────────────────────────────────────────────────
    print(" Fase 2 — Análisis Sintáctico (Parser)")

    parser       = ExpresionesParser(stream)
    err_sintax   = SintacticoErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(err_sintax)

    tree = parser.program()

    if err_sintax.hay_errores():
        print(f"  X  {len(err_sintax.errores)} error(es) sintáctico(s):\n")
        for e in err_sintax.errores:
            print(f"      {e}")
        print("\n ALTO Pipeline detenido — fase sintáctica.\n")
        sys.exit(1)

    print(" Sin errores sintácticos.\n")

    # ──────────────────────────────────────────────────────────
    # FASE 4 — ANÁLISIS SEMÁNTICO (Type Checker)
    # ──────────────────────────────────────────────────────────
    print(" Fase 3 — Análisis Semántico (Type Checking)")

    semantico = SemanticVisitor()
    semantico.visit(tree)

    if semantico.hay_errores():
        print(f"  X {len(semantico.errores)} error(es) semántico(s):\n")
        for e in semantico.errores:
            print(f"      {e}")
        print("\n ALTO Pipeline detenido — fase semántica.\n")
        sys.exit(1)

    print("  Sin errores semánticos.\n")

    # ──────────────────────────────────────────────────────────
    # FASE 5 — EJECUCIÓN (Intérprete)
    # ──────────────────────────────────────────────────────────
    print(" Fase 4 — Ejecución del Programa (Intérprete)")
    separador()

    interprete = InterpreterVisitor()
    try:
        interprete.visit(tree)
        print()
        separador()
        print(" OK - Pipeline completado exitosamente.\n")
    except Exception as e:
        print(f"\n X - Error en ejecución: {e}")
        print("ALTO - Pipeline detenido — error en intérprete.\n")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\nUso:     python pipeline.py <archivo>")
        print("Ejemplo: python pipeline.py programa.txt\n")
        sys.exit(1)

    main(sys.argv[1])