# ================================================================
# ir_manual.py
# Optimizador Manual de IR — Proyecto Final
# Aplica passes LLVM individuales usando el comando 'opt'
# Compatible con llvmlite 0.44+ (no usa PassManagerBuilder)
# ================================================================

import time
import subprocess
import tempfile
import os
import difflib


# ──────────────────────────────────────────────────────────────
# CATÁLOGO DE PASSES
# Cada entrada: clave → (descripcion, nombre_en_opt)
# Los nombres son compatibles con LLVM 15 (opt --passes=<nombre>)
# ──────────────────────────────────────────────────────────────

PASSES_INFO = {
    "mem2reg": (
        "Mem2Reg — Convierte allocas a registros SSA, "
        "elimina cargas/stores redundantes.",
        "mem2reg"
    ),
    "instcombine": (
        "Instruction Combining — Simplifica expresiones algebraicas "
        "(p.ej. x+0→x, x*1→x).",
        "instcombine"
    ),
    "simplifycfg": (
        "Simplify CFG — Elimina bloques básicos vacíos y "
        "simplifica el grafo de flujo de control.",
        "simplifycfg"
    ),
    "dce": (
        "Dead Code Elimination — Elimina código sin efecto "
        "en el resultado del programa.",
        "adce"
    ),
    "inline": (
        "Function Inlining — Sustituye llamadas a funciones pequeñas "
        "por el cuerpo inline (reduce overhead de llamada).",
        "inline"
    ),
    "constprop": (
        "Constant Propagation — Sustituye variables con valor constante "
        "por ese valor directamente.",
        "sccp"
    ),
    "gvn": (
        "Global Value Numbering — Elimina expresiones redundantes "
        "calculadas más de una vez.",
        "gvn"
    ),
    "loop-simplify": (
        "Loop Simplify — Normaliza la estructura de los bucles para "
        "facilitar otras optimizaciones.",
        "loop-simplify"
    ),
    "licm": (
        "Loop Invariant Code Motion — Mueve cálculos que no cambian "
        "entre iteraciones fuera del bucle.",
        "licm"
    ),
    "sroa": (
        "SROA — Scalar Replacement of Aggregates, reemplaza structs/arrays "
        "en stack por variables escalares.",
        "sroa"
    ),
}


# ──────────────────────────────────────────────────────────────
# FUNCIÓN PRINCIPAL: aplicar_passes
# ──────────────────────────────────────────────────────────────

def aplicar_passes(ir_texto: str, passes: list) -> dict:
    """
    Aplica una lista de passes LLVM sobre el módulo IR usando 'opt'.

    Parámetros:
        ir_texto (str)  : Código LLVM IR como string.
        passes   (list) : Lista de claves de PASSES_INFO.

    Retorna:
        ir_opt           (str)   : IR resultante
        diff             (str)   : Diff unified (original → manual)
        ok               (bool)  : True si no hubo errores
        tiempo_ms        (float) : Tiempo en ms
        error            (str)   : Mensaje de error si ok=False
        passes_aplicados (list)  : Passes que se ejecutaron
    """
    if not passes:
        return {
            "ir_opt":           ir_texto,
            "diff":             "",
            "ok":               True,
            "tiempo_ms":        0.0,
            "error":            None,
            "passes_aplicados": []
        }

    t0 = time.perf_counter()

    # Construir la cadena de passes para opt --passes=
    nombres_opt = []
    passes_validos = []
    for p in passes:
        if p in PASSES_INFO:
            _, nombre_opt = PASSES_INFO[p]
            nombres_opt.append(nombre_opt)
            passes_validos.append(p)

    if not nombres_opt:
        return {
            "ir_opt":           ir_texto,
            "diff":             "",
            "ok":               False,
            "tiempo_ms":        0.0,
            "error":            "Ningún pass válido seleccionado.",
            "passes_aplicados": []
        }

    # Crear archivos temporales
    fd_in, ruta_in   = tempfile.mkstemp(suffix='.ll', prefix='ir_man_in_')
    fd_out, ruta_out = tempfile.mkstemp(suffix='.ll', prefix='ir_man_out_')
    os.close(fd_out)

    try:
        with os.fdopen(fd_in, 'w', encoding='utf-8') as f:
            f.write(ir_texto)

        # Ejecutar: opt --passes="pass1,pass2" -S input.ll -o output.ll
        passes_str = ','.join(nombres_opt)
        res = subprocess.run(
            ['opt', f'--passes={passes_str}', '-S', ruta_in, '-o', ruta_out],
            capture_output=True,
            text=True,
            timeout=30
        )

        t1 = time.perf_counter()

        if res.returncode == 0 and os.path.exists(ruta_out):
            with open(ruta_out, 'r', encoding='utf-8') as f:
                ir_opt = f.read()
            diff = generar_diff(ir_texto, ir_opt)
            return {
                "ir_opt":           ir_opt,
                "diff":             diff,
                "ok":               True,
                "tiempo_ms":        round((t1 - t0) * 1000, 2),
                "error":            None,
                "passes_aplicados": passes_validos
            }
        else:
            # Fallback: intentar con sintaxis antigua (-mem2reg, -instcombine, ...)
            flags_old = [f'-{n}' for n in nombres_opt]
            res2 = subprocess.run(
                ['opt', '-S'] + flags_old + [ruta_in, '-o', ruta_out],
                capture_output=True, text=True, timeout=30
            )
            if res2.returncode == 0 and os.path.exists(ruta_out):
                with open(ruta_out, 'r', encoding='utf-8') as f:
                    ir_opt = f.read()
                diff = generar_diff(ir_texto, ir_opt)
                return {
                    "ir_opt":           ir_opt,
                    "diff":             diff,
                    "ok":               True,
                    "tiempo_ms":        round((t1 - t0) * 1000, 2),
                    "error":            None,
                    "passes_aplicados": passes_validos
                }
            return {
                "ir_opt":           ir_texto,
                "diff":             "",
                "ok":               False,
                "tiempo_ms":        round((t1 - t0) * 1000, 2),
                "error":            f"opt error: {res.stderr.strip() or res2.stderr.strip()}",
                "passes_aplicados": []
            }

    except FileNotFoundError:
        t1 = time.perf_counter()
        return {
            "ir_opt":           ir_texto,
            "diff":             "",
            "ok":               False,
            "tiempo_ms":        round((t1 - t0) * 1000, 2),
            "error":            "'opt' no encontrado. Instala: sudo apt install llvm",
            "passes_aplicados": []
        }
    except Exception as e:
        t1 = time.perf_counter()
        return {
            "ir_opt":           ir_texto,
            "diff":             "",
            "ok":               False,
            "tiempo_ms":        round((t1 - t0) * 1000, 2),
            "error":            str(e),
            "passes_aplicados": []
        }
    finally:
        for ruta in [ruta_in, ruta_out]:
            try:
                if os.path.exists(ruta):
                    os.remove(ruta)
            except Exception:
                pass


# ──────────────────────────────────────────────────────────────
# FUNCIÓN: generar_diff
# ──────────────────────────────────────────────────────────────

def generar_diff(ir_original: str, ir_optimizado: str) -> str:
    """Diff unified entre IR original e IR optimizado."""
    lineas_orig = ir_original.splitlines(keepends=True)
    lineas_opt  = ir_optimizado.splitlines(keepends=True)
    diff = difflib.unified_diff(
        lineas_orig, lineas_opt,
        fromfile="IR Original",
        tofile="IR Optimizado",
        n=3
    )
    return ''.join(diff)


# ──────────────────────────────────────────────────────────────
# FUNCIÓN: lista_passes_disponibles
# ──────────────────────────────────────────────────────────────

def lista_passes_disponibles() -> list:
    """Lista de passes para mostrar en la UI."""
    return [
        {"key": clave, "descripcion": desc, "tipo": "opt"}
        for clave, (desc, _) in PASSES_INFO.items()
    ]

