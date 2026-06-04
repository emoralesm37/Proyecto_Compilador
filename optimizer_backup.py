# ================================================================
# optimizer.py
# Optimizador LLVM IR — Proyecto Final
# Usa el comando 'opt -O3' vía subprocess.
# Compatible con llvmlite 0.44+ (PassManagerBuilder fue removido).
# Requiere: sudo apt install llvm  (para tener el comando 'opt')
# ================================================================

import time
import subprocess
import tempfile
import os


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

    fd_in,  ruta_in  = tempfile.mkstemp(suffix='.ll',    prefix='ir_orig_')
    fd_out, ruta_out = tempfile.mkstemp(suffix='_opt.ll', prefix='ir_opt_')
    os.close(fd_out)

    try:
        # Escribir el IR original al archivo temporal
        with os.fdopen(fd_in, 'w', encoding='utf-8') as f:
            f.write(ir_texto)

        # opt -O3 -S ir_original.ll -o ir_optimizado.ll
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
            "error":     "'opt' no encontrado. Instala con: sudo apt install llvm"
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
# Cuenta instrucciones/bloques analizando el texto del IR
# (no depende de llvmlite para mayor compatibilidad)
# ──────────────────────────────────────────────────────────────

def estadisticas_ir(ir_texto: str) -> dict:
    """Cuenta funciones, bloques e instrucciones en el texto IR."""
    if not ir_texto:
        return {"funciones": 0, "bloques": 0, "instrucciones": 0}

    funciones     = 0
    bloques       = 0
    instrucciones = 0

    for linea in ir_texto.splitlines():
        s = linea.strip()
        if s.startswith('define '):
            funciones += 1
        elif s.endswith(':') and not s.startswith(';') and not s.startswith('@'):
            bloques += 1
        elif (s and not s.startswith(';') and not s.startswith('}')
              and not s.startswith('{') and not s.startswith('@')
              and not s.startswith('define') and not s.startswith('declare')
              and not s.startswith('target') and not s.startswith('%')
              and ('=' in s or s.startswith('store ')
                   or s.startswith('ret ') or s.startswith('br ')
                   or s.startswith('call ') or s.startswith('switch '))):
            instrucciones += 1

    return {
        "funciones":     funciones,
        "bloques":       bloques,
        "instrucciones": instrucciones
    }