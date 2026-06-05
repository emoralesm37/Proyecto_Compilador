# ================================================================
# ir_manual.py
# Optimizador Manual de IR — Proyecto Final
# Permite seleccionar passes LLVM individuales y genera
# un diff (unified diff) entre el IR original y el optimizado.
# ================================================================

import time
import difflib

try:
    import llvmlite.binding as llvm
    _LLVM_DISPONIBLE = True
except Exception:
    _LLVM_DISPONIBLE = False


# ──────────────────────────────────────────────────────────────
# CATÁLOGO DE PASSES DISPONIBLES
# Cada entrada: nombre_clave → (descripción, tipo: 'module'|'function')
# ──────────────────────────────────────────────────────────────

PASSES_INFO = {
    "mem2reg": (
        "Mem2Reg / SROA — Convierte allocas a registros SSA, "
        "elimina cargas/stores redundantes.",
        "function"
    ),
    "instcombine": (
        "Instruction Combining — Combina instrucciones y simplifica expresiones "
        "algebraicas (p.ej. x+0→x, x*1→x).",
        "function"
    ),
    "simplifycfg": (
        "Simplify CFG — Elimina bloques básicos innecesarios, fusiona bloques vacíos "
        "y simplifica la estructura del grafo de flujo de control.",
        "function"
    ),
    "dce": (
        "Dead Code Elimination — Elimina código que no tiene efecto "
        "en el resultado del programa.",
        "function"
    ),
    "inline": (
        "Function Inlining — Sustituye llamadas a funciones pequeñas "
        "por el cuerpo de la función (reduce overhead de llamada).",
        "module"
    ),
    "constprop": (
        "Constant Propagation — Sustituye variables que siempre tienen "
        "el mismo valor constante por ese valor directamente.",
        "function"
    ),
    "gvn": (
        "Global Value Numbering — Elimina expresiones redundantes calculadas "
        "más de una vez en el mismo camino de ejecución.",
        "function"
    ),
    "loop-simplify": (
        "Loop Simplify — Normaliza la estructura de los bucles para facilitar "
        "otras optimizaciones de bucles.",
        "function"
    ),
    "sccp": (
        "Sparse Conditional Constant Propagation — Propagación de constantes "
        "más agresiva que considera condiciones de salto.",
        "function"
    ),
    "licm": (
        "Loop Invariant Code Motion — Mueve cálculos que no cambian "
        "entre iteraciones fuera del bucle.",
        "function"
    ),
}


# ──────────────────────────────────────────────────────────────
# FUNCIÓN PRINCIPAL: aplicar_passes
# ──────────────────────────────────────────────────────────────

def aplicar_passes(ir_texto: str, passes: list) -> dict:
    """
    Aplica una lista de passes LLVM manualmente sobre el módulo IR.

    Parámetros:
        ir_texto (str)  : Código LLVM IR como string.
        passes   (list) : Lista de claves de PASSES_INFO a aplicar.

    Retorna un diccionario con:
        ir_opt    (str)  : IR resultante después de los passes
        diff      (str)  : Diff unified entre IR original e IR optimizado
        ok        (bool) : True si no hubo errores
        tiempo_ms (float): Tiempo de aplicación en milisegundos
        error     (str|None): Mensaje de error si ok=False
        passes_aplicados (list): Passes que se ejecutaron
    """
    if not _LLVM_DISPONIBLE:
        return {
            "ir_opt":           ir_texto,
            "diff":             "",
            "ok":               False,
            "tiempo_ms":        0.0,
            "error":            "llvmlite no está instalado. Ejecuta: pip install llvmlite",
            "passes_aplicados": []
        }

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
    passes_aplicados = []

    try:
        mod = llvm.parse_assembly(ir_texto)
        mod.verify()

        # Separar passes por tipo
        passes_modulo   = [p for p in passes if _tipo_pass(p) == 'module']
        passes_funcion  = [p for p in passes if _tipo_pass(p) == 'function']

        # ── Passes a nivel de MÓDULO ──
        if passes_modulo:
            pm_mod = llvm.ModulePassManager()
            for p in passes_modulo:
                _agregar_pass_modulo(pm_mod, p)
                passes_aplicados.append(p)
            pm_mod.run(mod)

        # ── Passes a nivel de FUNCIÓN ──
        if passes_funcion:
            pm_func = llvm.FunctionPassManager(mod)
            for p in passes_funcion:
                _agregar_pass_funcion(pm_func, p)
                passes_aplicados.append(p)
            pm_func.initialize()
            for func in mod.functions:
                if not func.is_declaration:
                    pm_func.run(func)
            pm_func.finalize()

        ir_opt = str(mod)
        t1 = time.perf_counter()

        diff_texto = generar_diff(ir_texto, ir_opt)

        return {
            "ir_opt":           ir_opt,
            "diff":             diff_texto,
            "ok":               True,
            "tiempo_ms":        round((t1 - t0) * 1000, 2),
            "error":            None,
            "passes_aplicados": passes_aplicados
        }

    except Exception as e:
        t1 = time.perf_counter()
        return {
            "ir_opt":           ir_texto,
            "diff":             "",
            "ok":               False,
            "tiempo_ms":        round((t1 - t0) * 1000, 2),
            "error":            str(e),
            "passes_aplicados": passes_aplicados
        }


# ──────────────────────────────────────────────────────────────
# HELPERS INTERNOS
# ──────────────────────────────────────────────────────────────

def _tipo_pass(nombre: str) -> str:
    """Devuelve 'module' o 'function' según el tipo del pass."""
    return PASSES_INFO.get(nombre, ("", "function"))[1]


def _agregar_pass_modulo(pm, nombre: str):
    """Agrega un pass de módulo al ModulePassManager."""
    if nombre == "inline":
        pm.add_function_inlining_pass(225)
    elif nombre == "sccp":
        pm.add_ipsccp_pass()


def _agregar_pass_funcion(pm, nombre: str):
    """Agrega un pass de función al FunctionPassManager."""
    if nombre == "mem2reg":
        pm.add_sroa_pass()                       # SROA incluye mem2reg
    elif nombre == "instcombine":
        pm.add_instruction_combining_pass()
    elif nombre == "simplifycfg":
        pm.add_cfg_simplification_pass()
    elif nombre == "dce":
        pm.add_dead_code_elimination_pass()
    elif nombre == "constprop":
        pm.add_constant_propagation_pass()
    elif nombre == "gvn":
        pm.add_gvn_pass()
    elif nombre == "loop-simplify":
        pm.add_loop_simplification_pass()
    elif nombre == "sccp":
        pm.add_sccp_pass()
    elif nombre == "licm":
        pm.add_licm_pass()


# ──────────────────────────────────────────────────────────────
# FUNCIÓN: generar_diff
# ──────────────────────────────────────────────────────────────

def generar_diff(ir_original: str, ir_optimizado: str) -> str:
    """
    Genera un diff en formato unified entre el IR original y el optimizado.
    Las líneas añadidas comienzan con '+', las eliminadas con '-'.
    """
    lineas_orig = ir_original.splitlines(keepends=True)
    lineas_opt  = ir_optimizado.splitlines(keepends=True)

    diff = difflib.unified_diff(
        lineas_orig,
        lineas_opt,
        fromfile="IR Original",
        tofile="IR Optimizado",
        n=3
    )
    return ''.join(diff)


# ──────────────────────────────────────────────────────────────
# FUNCIÓN: lista_passes_disponibles
# ──────────────────────────────────────────────────────────────

def lista_passes_disponibles() -> list:
    """
    Retorna la lista de passes disponibles para mostrar en la UI.
    Cada elemento: { "key": str, "descripcion": str, "tipo": str }
    """
    return [
        {
            "key":         clave,
            "descripcion": desc,
            "tipo":        tipo
        }
        for clave, (desc, tipo) in PASSES_INFO.items()
    ]
