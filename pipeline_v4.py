# ================================================================
# pipeline_v4.py
# Orquestador Principal — Proyecto Final
# 8 Fases:
#   1. Léxico          — gramatica_v4Lexer
#   2. Sintáctico      — gramatica_v4Parser
#   3. Semántico       — semantic_visitor_v4
#   4. TAC             — tac_generator_v4
#   5. LLVM IR         — ir_generator_v4
#   6. Intérprete      — interpreter_visitor_v4
#   7. Optimizador O3  — optimizer (llvmlite PassManagerBuilder opt=3)
#   8. Generación Bin  — llc + clang (Linux .elf) / llc + mingw (Windows .exe)
# ================================================================

import sys
import io
import os
import time
import subprocess
import tempfile
from contextlib import redirect_stdout

from antlr4 import *
from antlr4.InputStream import InputStream

from errores_personalizados import LexicoErrorListener, SintacticoErrorListener
from gramatica_v4Lexer   import gramatica_v4Lexer
from gramatica_v4Parser  import gramatica_v4Parser
from errores_personalizados import LexicoErrorListener, SintacticoErrorListener
from semantic_visitor_v4  import SemanticVisitor
from tac_generator_v4     import TACGenerator
from ir_generator_v4      import IRGenerator
from interpreter_visitor_v4 import InterpreterVisitor
from optimizer_VA            import optimizar_o3


# ──────────────────────────────────────────────────────────────
# CONSTANTES
# ──────────────────────────────────────────────────────────────
OK    = "OK"
ERROR = "ERROR"
SKIP  = "SKIP"   # Fase omitida porque dependencia anterior falló


# ──────────────────────────────────────────────────────────────
# FUNCIÓN PRINCIPAL: run_pipeline
# ──────────────────────────────────────────────────────────────

def run_pipeline(codigo: str,
                 archivo_base: str = "programa",
                 generar_binarios: bool = False,
                 plataformas: list = None) -> dict:
    """
    Ejecuta las 8 fases del compilador.

    Parámetros:
        codigo           (str)  : Código fuente a compilar.
        archivo_base     (str)  : Ruta base para archivos de salida (.tac, .ll, .elf, .exe).
        generar_binarios (bool) : Si True, ejecuta la Fase 8 para generar binarios.
        plataformas      (list) : Lista con 'linux' y/o 'windows' para la Fase 8.

    Retorna un dict con:
        fases        (list)  : [{nombre, estado, tiempo_ms, errores}]
        tac          (str)   : Código TAC generado
        ir           (str)   : LLVM IR original
        ir_opt       (str)   : LLVM IR optimizado (O3)
        consola      (list)  : Salida del intérprete
        ir_out       (list)  : Salida de lli
        binarios     (dict)  : {linux: ruta|"", windows: ruta|""}
        stats_orig   (dict)  : Estadísticas del IR original
        stats_opt    (dict)  : Estadísticas del IR optimizado
        ok           (bool)  : True si las fases 1-6 completaron sin errores
    """
    if plataformas is None:
        plataformas = ['linux']

    resultado = {
        "fases":      [],
        "tac":        "",
        "ir":         "",
        "ir_opt":     "",
        "consola":    [],
        "ir_out":     [],
        "binarios":   {"linux": "", "windows": ""},
        "stats_orig": {},
        "stats_opt":  {},
        "ok":         False,
    }

    def fase(nombre, estado, tiempo_ms, errores=None):
        resultado["fases"].append({
            "nombre":    nombre,
            "estado":    estado,
            "tiempo_ms": round(tiempo_ms, 2),
            "errores":   errores or [],
        })

    os.makedirs(os.path.dirname(archivo_base) if os.path.dirname(archivo_base) else ".", exist_ok=True)

    # ──────────────────────────────────────────────────────────
    # FASE 1 — ANÁLISIS LÉXICO
    # ──────────────────────────────────────────────────────────
    t0 = time.perf_counter()

    input_stream = InputStream(codigo)
    lexer        = gramatica_v4Lexer(input_stream)
    err_lexico   = LexicoErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(err_lexico)

    stream = CommonTokenStream(lexer)
    stream.fill()

    ms = (time.perf_counter() - t0) * 1000
    if err_lexico.hay_errores():
        fase("Léxico", ERROR, ms, err_lexico.errores)
        return resultado
    fase("Léxico", OK, ms)

    # ──────────────────────────────────────────────────────────
    # FASE 2 — ANÁLISIS SINTÁCTICO
    # ──────────────────────────────────────────────────────────
    t0 = time.perf_counter()

    parser     = gramatica_v4Parser(stream)
    err_sintax = SintacticoErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(err_sintax)
    tree = parser.program()

    ms = (time.perf_counter() - t0) * 1000
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

    ms = (time.perf_counter() - t0) * 1000
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
        tac_gen.guardar(f"{archivo_base}.tac")
        fase("TAC", OK, (time.perf_counter() - t0) * 1000)
    except Exception as e:
        fase("TAC", ERROR, (time.perf_counter() - t0) * 1000, [str(e)])
        return resultado

    # ──────────────────────────────────────────────────────────
    # FASE 5 — GENERACIÓN DE LLVM IR
    # ──────────────────────────────────────────────────────────
    t0 = time.perf_counter()
    ruta_ll = f"{archivo_base}.ll"
    try:
        ir_gen = IRGenerator()
        ir_gen.visit(tree)
        ir_texto = ir_gen.obtener_ir()
        resultado["ir"] = ir_texto
        ir_gen.guardar(ruta_ll)

        # Intentar ejecutar con lli
        try:
            proc = subprocess.run(
                ["lli", ruta_ll],
                capture_output=True, text=True, timeout=10
            )
            resultado["ir_out"] = proc.stdout.splitlines()
        except (FileNotFoundError, subprocess.TimeoutExpired):
            resultado["ir_out"] = ["[lli no disponible o timeout]"]

        fase("LLVM IR", OK, (time.perf_counter() - t0) * 1000)
    except Exception as e:
        fase("LLVM IR", ERROR, (time.perf_counter() - t0) * 1000, [str(e)])
        return resultado

    # ──────────────────────────────────────────────────────────
    # FASE 6 — INTÉRPRETE
    # ──────────────────────────────────────────────────────────
    t0 = time.perf_counter()
    buffer = io.StringIO()
    try:
        with redirect_stdout(buffer):
            interprete = InterpreterVisitor()
            interprete.visit(tree)
        resultado["consola"] = buffer.getvalue().splitlines()
        fase("Intérprete", OK, (time.perf_counter() - t0) * 1000)
    except Exception as e:
        resultado["consola"] = buffer.getvalue().splitlines()
        fase("Intérprete", ERROR, (time.perf_counter() - t0) * 1000, [str(e)])
        return resultado

    # Todas las fases 1–6 pasaron
    resultado["ok"] = True

    # ──────────────────────────────────────────────────────────
    # FASE 7 — OPTIMIZADOR LLVM O3
    # ──────────────────────────────────────────────────────────
    t0 = time.perf_counter()
    try:
        from optimizer_VA import estadisticas_ir
        resultado["stats_orig"] = estadisticas_ir(ir_texto)

        opt_result = optimizar_o3(ir_texto)
        ir_opt = opt_result["ir_opt"]
        resultado["ir_opt"] = ir_opt

        # Guardar IR optimizado
        ruta_ll_opt = f"{archivo_base}_opt.ll"
        with open(ruta_ll_opt, 'w', encoding='utf-8') as f:
            f.write(ir_opt)

        resultado["stats_opt"] = estadisticas_ir(ir_opt)

        if opt_result["ok"]:
            fase("Optimizador O3", OK, opt_result["tiempo_ms"])
        else:
            fase("Optimizador O3", ERROR,
                 opt_result["tiempo_ms"], [opt_result.get("error", "")])
    except Exception as e:
        fase("Optimizador O3", ERROR, (time.perf_counter() - t0) * 1000, [str(e)])

    # ──────────────────────────────────────────────────────────
    # FASE 8 — GENERACIÓN DE BINARIOS
    # ──────────────────────────────────────────────────────────
    if generar_binarios:
        t0 = time.perf_counter()
        errores_bin = []
        ir_para_bin = resultado["ir_opt"] or resultado["ir"]

        for plataforma in plataformas:
            exito, ruta, err = _generar_binario(
                ir_texto=ir_para_bin,
                archivo_base=archivo_base,
                plataforma=plataforma
            )
            if exito:
                resultado["binarios"][plataforma] = ruta
            else:
                errores_bin.append(f"[{plataforma}] {err}")

        ms = (time.perf_counter() - t0) * 1000
        estado = OK if not errores_bin else ERROR
        fase("Generación Binarios", estado, ms, errores_bin)
    else:
        fase("Generación Binarios", SKIP, 0.0,
             ["Omitida — activa 'Generar Binarios' para compilar."])

    return resultado


# ──────────────────────────────────────────────────────────────
# GENERACIÓN DE BINARIOS
# ──────────────────────────────────────────────────────────────

def _generar_binario(ir_texto: str,
                     archivo_base: str,
                     plataforma: str) -> tuple:
    """
    Genera un binario nativo a partir del IR optimizado.

    Plataformas soportadas:
        'linux'   → usa llc + clang → archivo .elf
        'windows' → usa llc (mtriple mingw) + x86_64-w64-mingw32-gcc → .exe

    Retorna (exito: bool, ruta_binario: str, error: str)
    """
    try:
        # Escribir IR a archivo temporal
        fd, ruta_ll = tempfile.mkstemp(suffix=".ll")
        with os.fdopen(fd, 'w') as f:
            f.write(ir_texto)

        if plataforma == 'linux':
            return _binario_linux(ruta_ll, archivo_base)
        elif plataforma == 'windows':
            return _binario_windows(ruta_ll, archivo_base)
        else:
            return False, "", f"Plataforma '{plataforma}' no soportada."

    except Exception as e:
        return False, "", str(e)
    finally:
        if os.path.exists(ruta_ll):
            try:
                os.remove(ruta_ll)
            except Exception:
                pass


def _binario_linux(ruta_ll: str, archivo_base: str) -> tuple:
    """
    Linux .elf: llc -filetype=obj → clang → ejecutable
    """
    ruta_obj = f"{archivo_base}_linux.o"
    ruta_elf = f"{archivo_base}.elf"

    # Paso 1: IR → objeto
    res = subprocess.run(
        ["llc", "-filetype=obj", "-o", ruta_obj, ruta_ll],
        capture_output=True, text=True, timeout=30
    )
    if res.returncode != 0:
        return False, "", f"llc (linux): {res.stderr}"

    # Paso 2: objeto → ejecutable
    res = subprocess.run(
        ["clang", ruta_obj, "-o", ruta_elf],
        capture_output=True, text=True, timeout=30
    )
    if res.returncode != 0:
        # Intentar con gcc como fallback
        res2 = subprocess.run(
            ["gcc", ruta_obj, "-o", ruta_elf],
            capture_output=True, text=True, timeout=30
        )
        if res2.returncode != 0:
            return False, "", f"clang/gcc (linux): {res.stderr} | {res2.stderr}"

    # Limpiar objeto
    try:
        os.remove(ruta_obj)
    except Exception:
        pass

    return True, ruta_elf, ""


def _binario_windows(ruta_ll: str, archivo_base: str) -> tuple:
    """
    Windows .exe: llc -mtriple=x86_64-pc-windows-gnu -filetype=obj
                  → x86_64-w64-mingw32-gcc → .exe
    """
    ruta_obj = f"{archivo_base}_win.o"
    ruta_exe = f"{archivo_base}.exe"

    # Paso 1: IR → objeto COFF (formato Windows)
    res = subprocess.run(
        ["llc",
         "-mtriple=x86_64-pc-windows-gnu",
         "-filetype=obj",
         "-o", ruta_obj,
         ruta_ll],
        capture_output=True, text=True, timeout=30
    )
    if res.returncode != 0:
        return False, "", f"llc (windows): {res.stderr}"

    # Paso 2: objeto → .exe con MinGW
    res = subprocess.run(
        ["x86_64-w64-mingw32-gcc", ruta_obj, "-o", ruta_exe],
        capture_output=True, text=True, timeout=30
    )
    if res.returncode != 0:
        return False, "", f"mingw-gcc: {res.stderr}"

    # Limpiar objeto
    try:
        os.remove(ruta_obj)
    except Exception:
        pass

    return True, ruta_exe, ""


# ──────────────────────────────────────────────────────────────
# MODO CLI
# ──────────────────────────────────────────────────────────────

def main_cli(archivo: str, generar_binarios: bool = False):
    print("═" * 60)
    print("  Pipeline de Compilación v4 — Proyecto Final")
    print(f"  Archivo : {archivo}")
    print("  Fases   : Léxico → Sintáctico → Semántico → TAC")
    print("            → LLVM IR → Intérprete → Opt O3 → Binarios")
    print("═" * 60 + "\n")

    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
    except FileNotFoundError:
        print(f"  X No se encontró el archivo: '{archivo}'")
        sys.exit(1)

    archivo_base = os.path.splitext(archivo)[0]
    resultado    = run_pipeline(
        codigo, archivo_base,
        generar_binarios=generar_binarios,
        plataformas=['linux', 'windows'] if generar_binarios else []
    )

    iconos = {OK: "OK", ERROR: "X", SKIP: "○"}
    for i, f in enumerate(resultado["fases"], 1):
        icono = iconos.get(f["estado"], "?")
        print(f"  {icono} Fase {i} — {f['nombre']:22} [{f['estado']}]  {f['tiempo_ms']:.2f} ms")
        for e in f["errores"]:
            print(f"      → {e}")

    print()

    if resultado["stats_orig"]:
        s = resultado["stats_orig"]
        print(f"  IR Original : {s['instrucciones']} instrucciones, {s['bloques']} bloques")
    if resultado["stats_opt"]:
        s = resultado["stats_opt"]
        print(f"  IR Opt O3   : {s['instrucciones']} instrucciones, {s['bloques']} bloques")

    if resultado["binarios"]["linux"]:
        print(f"  Binario Linux  : {resultado['binarios']['linux']}")
    if resultado["binarios"]["windows"]:
        print(f"  Binario Windows: {resultado['binarios']['windows']}")

    if resultado["ok"]:
        print("\n" + "═" * 60)
        print("  OK - Pipeline completado exitosamente.")
        print("═" * 60)
    else:
        print("\n  X - Pipeline detenido por errores.")


if __name__ == '__main__':
    _generar = '--binarios' in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print("\nUso:     python pipeline_v4.py <archivo> [--binarios]")
        print("Ejemplo: python pipeline_v4.py programa.src --binarios\n")
        sys.exit(1)
    main_cli(args[0], generar_binarios=_generar)