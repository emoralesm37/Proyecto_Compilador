# ================================================================
# pipeline.py  (v3)
# Orquestador principal — Proyecto 3
# Fases: Léxico → Sintáctico → Semántico → TAC → LLVM IR → Intérprete
# Uso CLI:  python pipeline.py <archivo_entrada>
# Uso API:  resultado = run_pipeline(codigo_fuente: str) -> dict
# ================================================================

import sys
import time
import subprocess
import tempfile
import os

from antlr4 import *
from antlr4.InputStream import InputStream

from gramatica_v3Lexer   import gramatica_v3Lexer
from gramatica_v3Parser  import gramatica_v3Parser
from errores_personalizados        import LexicoErrorListener, SintacticoErrorListener
from semantic_visitor     import SemanticVisitor
from tac_generator        import TACGenerator
from ir_generator         import IRGenerator
from interpreter_visitor  import InterpreterVisitor


# ──────────────────────────────────────────────────────────────
# CONSTANTES DE ESTADO
# ──────────────────────────────────────────────────────────────
OK    = "OK"
ERROR = "ERROR"


# ──────────────────────────────────────────────────────────────
# FUNCIÓN PRINCIPAL: run_pipeline
# Acepta código como string; retorna un dict con todos los resultados.
# La interfaz Flask la llama directamente.
# ──────────────────────────────────────────────────────────────

def run_pipeline(codigo: str, archivo_base: str = "programa") -> dict:
    """
    Ejecuta las 6 fases del compilador sobre `codigo`.
    Retorna un diccionario con:
      - fases:   lista de {nombre, estado, tiempo_ms, errores}
      - tac:     string con el TAC generado (o "")
      - ir:      string con el LLVM IR generado (o "")
      - consola: lista de strings (output del intérprete)
      - ir_out:  lista de strings (output de lli)
      - ok:      bool — True si todas las fases pasaron
    """

    resultado = {
        "fases":   [],
        "tac":     "",
        "ir":      "",
        "consola": [],
        "ir_out":  [],
        "ok":      False,
    }

    def fase(nombre, estado, tiempo_ms, errores=None):
        resultado["fases"].append({
            "nombre":    nombre,
            "estado":    estado,
            "tiempo_ms": round(tiempo_ms, 2),
            "errores":   errores or [],
        })

    # ──────────────────────────────────────────────────────────
    # FASE 1 — ANÁLISIS LÉXICO
    # ──────────────────────────────────────────────────────────
    t0 = time.perf_counter()

    input_stream = InputStream(codigo)
    lexer        = gramatica_v3Lexer(input_stream)
    err_lexico   = LexicoErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(err_lexico)

    stream = CommonTokenStream(lexer)
    stream.fill()

    t1 = time.perf_counter()
    ms = (t1 - t0) * 1000

    if err_lexico.hay_errores():
        fase("Léxico", ERROR, ms, err_lexico.errores)
        return resultado

    fase("Léxico", OK, ms)

    # ──────────────────────────────────────────────────────────
    # FASE 2 — ANÁLISIS SINTÁCTICO
    # ──────────────────────────────────────────────────────────
    t0 = time.perf_counter()

    parser     = gramatica_v3Parser(stream)
    err_sintax = SintacticoErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(err_sintax)

    tree = parser.program()

    t1 = time.perf_counter()
    ms = (t1 - t0) * 1000

    if err_sintax.hay_errores():
        fase("Sintáctico", ERROR, ms, err_sintax.errores)
        return resultado

    fase("Sintáctico", OK, ms)

    # ──────────────────────────────────────────────────────────
    # FASE 3 — ANÁLISIS SEMÁNTICO
    # ──────────────────────────────────────────────────────────
    t0 = time.perf_counter()

    semantico = SemanticVisitor()
    semantico.visit(tree)

    t1 = time.perf_counter()
    ms = (t1 - t0) * 1000

    if semantico.hay_errores():
        fase("Semántico", ERROR, ms, semantico.errores)
        return resultado

    fase("Semántico", OK, ms)

    # ──────────────────────────────────────────────────────────
    # FASE 4 — GENERACIÓN DE TAC
    # ──────────────────────────────────────────────────────────
    t0 = time.perf_counter()

    try:
        tac_gen = TACGenerator()
        tac_gen.visit(tree)
        tac_texto = tac_gen.obtener_texto()
        resultado["tac"] = tac_texto

        # Guardar archivo .tac
        ruta_tac = f"{archivo_base}.tac"
        tac_gen.guardar(ruta_tac)

        t1 = time.perf_counter()
        fase("TAC", OK, (t1 - t0) * 1000)

    except Exception as e:
        t1 = time.perf_counter()
        fase("TAC", ERROR, (t1 - t0) * 1000, [str(e)])
        return resultado

    # ──────────────────────────────────────────────────────────
    # FASE 5 — GENERACIÓN DE LLVM IR
    # ──────────────────────────────────────────────────────────
    t0 = time.perf_counter()

    try:
        ir_gen = IRGenerator()
        ir_gen.visit(tree)
        ir_texto = ir_gen.obtener_ir()
        resultado["ir"] = ir_texto

        # Guardar archivo .ll
        ruta_ll = f"{archivo_base}.ll"
        ir_gen.guardar(ruta_ll)

        t1 = time.perf_counter()
        fase("LLVM IR", OK, (t1 - t0) * 1000)

        # Intentar ejecutar con lli (si está instalado)
        try:
            proc = subprocess.run(
                ["lli", ruta_ll],
                capture_output=True, text=True, timeout=10
            )
            resultado["ir_out"] = proc.stdout.splitlines()
        except (FileNotFoundError, subprocess.TimeoutExpired):
            resultado["ir_out"] = ["[lli no disponible o timeout]"]

    except Exception as e:
        t1 = time.perf_counter()
        fase("LLVM IR", ERROR, (t1 - t0) * 1000, [str(e)])
        return resultado

    # ──────────────────────────────────────────────────────────
    # FASE 6 — INTÉRPRETE (captura stdout)
    # ──────────────────────────────────────────────────────────
    t0 = time.perf_counter()

    import io
    from contextlib import redirect_stdout

    buffer = io.StringIO()
    try:
        with redirect_stdout(buffer):
            interprete = InterpreterVisitor()
            interprete.visit(tree)

        t1 = time.perf_counter()
        resultado["consola"] = buffer.getvalue().splitlines()
        fase("Intérprete", OK, (t1 - t0) * 1000)

    except Exception as e:
        t1 = time.perf_counter()
        resultado["consola"] = buffer.getvalue().splitlines()
        fase("Intérprete", ERROR, (t1 - t0) * 1000, [str(e)])
        return resultado

    resultado["ok"] = True
    return resultado


# ──────────────────────────────────────────────────────────────
# MODO CLI — uso directo desde la terminal
# ──────────────────────────────────────────────────────────────

def _separador(char="─", ancho=55):
    print(char * ancho)

def _titulo(texto, char="═"):
    _separador(char)
    print(f"  {texto}")
    _separador(char)


def main_cli(archivo: str):
    _titulo("Pipeline de Compilación v3")
    print(f"  Archivo : {archivo}")
    print(f"  Fases   : Léxico → Sintáctico → Semántico → TAC → LLVM IR → Intérprete")
    _separador("═")
    print()

    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
    except FileNotFoundError:
        print(f"  ✗ No se encontró el archivo: '{archivo}'")
        sys.exit(1)

    archivo_base = os.path.splitext(archivo)[0]
    resultado    = run_pipeline(codigo, archivo_base)

    # Mostrar resultados por fase
    iconos = {OK: "✓", ERROR: "✗"}
    for i, f in enumerate(resultado["fases"], 1):
        icono = iconos[f["estado"]]
        print(f"  Fase {i} — {f['nombre']:12} [{f['estado']}]  {f['tiempo_ms']:.2f} ms")
        if f["errores"]:
            for e in f["errores"]:
                print(f"      → {e}")

    print()

    if resultado["tac"]:
        _separador()
        print("  TAC generado:")
        _separador()
        print(resultado["tac"])
        print()

    if resultado["consola"]:
        _separador()
        print("  Salida del intérprete:")
        _separador()
        for linea in resultado["consola"]:
            print(f"  {linea}")
        print()

    if resultado["ir_out"]:
        _separador()
        print("  Salida de lli (LLVM IR):")
        _separador()
        for linea in resultado["ir_out"]:
            print(f"  {linea}")
        print()

    if resultado["ok"]:
        _separador("═")
        print("  ✓ Pipeline completado exitosamente.")
        _separador("═")
    else:
        print("\n  ✗ Pipeline detenido por errores.")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\nUso:     python pipeline.py <archivo>")
        print("Ejemplo: python pipeline.py programa.src\n")
        sys.exit(1)
    main_cli(sys.argv[1])
