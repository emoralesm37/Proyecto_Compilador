# ================================================================
# optimizer.py
# Optimizador LLVM IR — Proyecto Final
# Usa llvmlite.binding para aplicar el nivel de optimización O3
# sobre el módulo IR generado por ir_generator_v4.py
# ================================================================

import time

try:
    import llvmlite.binding as llvm

    # Inicialización única de LLVM (solo la primera vez que se importa)
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
    Aplica el nivel de optimización O3 de LLVM al módulo IR dado.

    Parámetros:
        ir_texto (str): Código LLVM IR como string (salida de IRGenerator).

    Retorna un diccionario con:
        ir_opt    (str)   : IR optimizado
        ok        (bool)  : True si no hubo errores
        tiempo_ms (float) : Tiempo de optimización en milisegundos
        error     (str|None): Mensaje de error si ok=False
    """
    if not _LLVM_DISPONIBLE:
        return {
            "ir_opt":    ir_texto,
            "ok":        False,
            "tiempo_ms": 0.0,
            "error":     "llvmlite no está instalado. Ejecuta: pip install llvmlite"
        }

    t0 = time.perf_counter()
    try:
        # 1. Parsear el texto IR
        mod = llvm.parse_assembly(ir_texto)
        mod.verify()

        # 2. Configurar opciones O3
        pto = llvm.create_pipeline_tuning_options()
        pto.speed_level = 3
        pto.size_level = 0
        pto.loop_vectorization = True
        pto.slp_vectorization = True
        pto.loop_unrolling = True

        # 3. Crear TargetMachine
        target = llvm.Target.from_default_triple()
        tm = target.create_target_machine()

        # 4. Crear PassBuilder
        pb = llvm.create_pass_builder(tm, pto)

        # 5. Obtener Module Pass Manager
        pm = pb.getModulePassManager()

        # 6. Ejecutar optimización
        pm.run(mod, pb)

        ir_opt = str(mod)
        t1 = time.perf_counter()

        return {
            "ir_opt": ir_opt,
            "ok": True,
            "tiempo_ms": round((t1 - t0) * 1000, 2),
            "error": None
        }

    except Exception as e:
        t1 = time.perf_counter()

        return {
            "ir_opt": ir_texto,
            "ok": False,
            "tiempo_ms": round((t1 - t0) * 1000, 2),
            "error": str(e)
        }
    
# ──────────────────────────────────────────────────────────────
# FUNCIÓN AUXILIAR: estadisticas_ir
# Cuenta instrucciones y bloques básicos en un módulo IR
# ──────────────────────────────────────────────────────────────

def estadisticas_ir(ir_texto: str) -> dict:
    """
    Devuelve estadísticas básicas del IR (instrucciones, bloques, funciones).
    Útil para comparar antes y después de la optimización.
    """
    if not _LLVM_DISPONIBLE or not ir_texto:
        return {"funciones": 0, "bloques": 0, "instrucciones": 0}

    try:
        mod = llvm.parse_assembly(ir_texto)
        funciones    = 0
        bloques      = 0
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
