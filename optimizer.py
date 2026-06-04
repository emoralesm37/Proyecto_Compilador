# ================================================================
# optimizer.py
# Optimizador LLVM IR — Proyecto Final
# Usa el comando 'opt' vía subprocess (compatible llvmlite 0.44+)
# 'opt' viene incluido con: sudo apt install llvm
# ================================================================

import time
import subprocess
import tempfile
import os

try:
    import llvmlite.binding as llvm

    # Inicialización única de LLVM (solo la primera vez que se importa)
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()
    _LLVM_DISPONIBLE = True
except Exception:
    _LLVM_DISPONIBLE = False
    
# ──────────────────────────────────────────────────────────────
# FUNCIÓN PRINCIPAL: optimizar_o3
# ──────────────────────────────────────────────────────────────

def optimizar_o3(ir_texto: str) -> dict:
    """
    Aplica optimización O3 al IR usando el comando 'opt -O3'.

    Retorna:
        ir_opt    (str)      : IR optimizado
        ok        (bool)     : True si no hubo errores
        tiempo_ms (float)    : Tiempo en ms
        error     (str|None) : Mensaje de error si ok=False
    """
    t0 = time.perf_counter()

    # Crear archivos temporales
    fd_in, ruta_in   = tempfile.mkstemp(suffix='.ll',     prefix='ir_orig_')
    fd_out, ruta_out = tempfile.mkstemp(suffix='_opt.ll',  prefix='ir_opt_')
    os.close(fd_out)

    try:
        # Escribir IR original al archivo temporal
        with os.fdopen(fd_in, 'w', encoding='utf-8') as f:
            f.write(ir_texto)

        # Ejecutar: opt -O3 -S ir_original.ll -o ir_optimizado.ll
        res = subprocess.run(
            ['opt', '-O3', '-S', ruta_in, '-o', ruta_out],
            capture_output=True,
            text=True,
            timeout=30
        )

        t1 = time.perf_counter()

        if res.returncode == 0 and os.path.exists(ruta_out):
            with open(ruta_out, 'r', encoding='utf-8') as f:
                ir_opt = f.read()
            return {
                "ir_opt":    ir_opt,
                "ok":        True,
                "tiempo_ms": round((t1 - t0) * 1000, 2),
                "error":     None
            }
        else:
            return {
                "ir_opt":    ir_texto,
                "ok":        False,
                "tiempo_ms": round((t1 - t0) * 1000, 2),
                "error":     f"opt falló (código {res.returncode}): {res.stderr.strip()}"
            }

    except FileNotFoundError:
        t1 = time.perf_counter()
        return {
            "ir_opt":    ir_texto,
            "ok":        False,
            "tiempo_ms": round((t1 - t0) * 1000, 2),
            "error":     "'opt' no encontrado. Instala: sudo apt install llvm"
        }
    except subprocess.TimeoutExpired:
        t1 = time.perf_counter()
        return {
            "ir_opt":    ir_texto,
            "ok":        False,
            "tiempo_ms": round((t1 - t0) * 1000, 2),
            "error":     "opt tardó demasiado (timeout 30s)"
        }
    except Exception as e:
        t1 = time.perf_counter()
        return {
            "ir_opt":    ir_texto,
            "ok":        False,
            "tiempo_ms": round((t1 - t0) * 1000, 2),
            "error":     str(e)
        }
    finally:
        for ruta in [ruta_in, ruta_out]:
            try:
                if os.path.exists(ruta):
                    os.remove(ruta)
            except Exception:
                pass


# ──────────────────────────────────────────────────────────────
# FUNCIÓN AUXILIAR: estadisticas_ir
# Cuenta instrucciones y bloques en el texto IR
# ──────────────────────────────────────────────────────────────

def estadisticas_ir(ir_texto: str) -> dict:
    """
    Cuenta funciones, bloques básicos e instrucciones en el IR.
    Usa análisis de texto (no depende de llvmlite).
    """
    if not ir_texto:
        return {"funciones": 0, "bloques": 0, "instrucciones": 0}

    funciones     = 0
    bloques       = 0
    instrucciones = 0

    for linea in ir_texto.splitlines():
        linea_strip = linea.strip()
        if linea_strip.startswith('define '):
            funciones += 1
        elif linea_strip.endswith(':') and not linea_strip.startswith(';'):
            # Etiqueta de bloque básico
            bloques += 1
        elif linea_strip and not linea_strip.startswith(';') \
                and not linea_strip.startswith('@') \
                and not linea_strip.startswith('%') \
                and not linea_strip.startswith('}') \
                and not linea_strip.startswith('{') \
                and '=' in linea_strip or linea_strip.startswith('store ') \
                or linea_strip.startswith('ret ') \
                or linea_strip.startswith('br ') \
                or linea_strip.startswith('call ') \
                or linea_strip.startswith('switch '):
            instrucciones += 1

    return {
        "funciones":     funciones,
        "bloques":       bloques,
        "instrucciones": instrucciones
    }
