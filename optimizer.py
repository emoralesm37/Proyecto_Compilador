# ================================================================
# optimizer.py
# Optimizador LLVM IR — Proyecto Final
# Usa llvmlite.binding para aplicar el nivel de optimización O3
# ================================================================

import time

# Inicialización lazy — se ejecuta solo cuando se llama por primera vez
_LLVM_ESTADO = None    # None=no checkeado, True=OK, False=error
_LLVM_ERROR  = ""
_llvm        = None    # referencia al módulo llvmlite.binding


def _inicializar_llvm() -> bool:
    """
    Inicializa LLVM una sola vez.
    Retorna True si está disponible, False si hay error.
    """
    global _LLVM_ESTADO, _LLVM_ERROR, _llvm
    if _LLVM_ESTADO is not None:
        return _LLVM_ESTADO

    try:
        import llvmlite.binding as llvm
        # llvmlite 0.44+ inicializa LLVM automáticamente al importar
        # las llamadas a initialize() fueron eliminadas en esta versión
        _llvm        = llvm
        _LLVM_ESTADO = True
        return True
    except ImportError as e:
        _LLVM_ERROR  = f"llvmlite no instalado: {e}. Ejecuta: pip install llvmlite"
        _LLVM_ESTADO = False
        return False
    except Exception as e:
        _LLVM_ERROR  = f"Error al inicializar LLVM: {e}"
        _LLVM_ESTADO = False
        return False


# ──────────────────────────────────────────────────────────────
# FUNCIÓN PRINCIPAL: optimizar_o3
# ──────────────────────────────────────────────────────────────

def optimizar_o3(ir_texto: str) -> dict:
    """
    Aplica el nivel de optimización O3 de LLVM al módulo IR dado.

    Retorna:
        ir_opt    (str)        : IR optimizado
        ok        (bool)       : True si no hubo errores
        tiempo_ms (float)      : Tiempo en ms
        error     (str|None)   : Mensaje de error si ok=False
    """
    if not _inicializar_llvm():
        return {
            "ir_opt":    ir_texto,
            "ok":        False,
            "tiempo_ms": 0.0,
            "error":     _LLVM_ERROR
        }

    llvm = _llvm
    t0   = time.perf_counter()

    try:
        # 1. Parsear el texto IR
        mod = llvm.parse_assembly(ir_texto)
        mod.verify()

        # 2. Configurar PassManagerBuilder con nivel O3
        pmb = llvm.PassManagerBuilder()
        pmb.opt_level          = 3
        pmb.loop_vectorize     = True
        pmb.slp_vectorize      = True
        pmb.inlining_threshold = 275

        # 3. Crear módulo pass manager y poblar con los passes O3
        pm = llvm.ModulePassManager()
        pmb.populate(pm)

        # 4. Ejecutar optimización
        pm.run(mod)

        ir_opt = str(mod)
        t1     = time.perf_counter()

        return {
            "ir_opt":    ir_opt,
            "ok":        True,
            "tiempo_ms": round((t1 - t0) * 1000, 2),
            "error":     None
        }

    except Exception as e:
        t1 = time.perf_counter()
        return {
            "ir_opt":    ir_texto,
            "ok":        False,
            "tiempo_ms": round((t1 - t0) * 1000, 2),
            "error":     f"Error en optimización O3: {e}"
        }


# ──────────────────────────────────────────────────────────────
# FUNCIÓN AUXILIAR: estadisticas_ir
# ──────────────────────────────────────────────────────────────

def estadisticas_ir(ir_texto: str) -> dict:
    """
    Devuelve estadísticas del IR: funciones, bloques, instrucciones.
    """
    if not _inicializar_llvm() or not ir_texto:
        return {"funciones": 0, "bloques": 0, "instrucciones": 0}

    llvm = _llvm
    try:
        mod           = llvm.parse_assembly(ir_texto)
        funciones     = 0
        bloques       = 0
        instrucciones = 0

        for func in mod.functions:
            if not func.is_declaration:
                funciones += 1
                for blk in func.blocks:
                    bloques += 1
                    for _ in blk.instructions:
                        instrucciones += 1

        return {
            "funciones":     funciones,
            "bloques":       bloques,
            "instrucciones": instrucciones
        }
    except Exception:
        return {"funciones": 0, "bloques": 0, "instrucciones": 0}