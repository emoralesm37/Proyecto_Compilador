# ================================================================
# ui_compiler_v4.py
# Interfaz Web del Compilador — Proyecto Final
# Servidor Flask con endpoints para:
#   POST /compilar          → Pipeline completo (8 fases)
#   POST /optimizar_manual  → Optimización con passes individuales
#   POST /generar_binario   → Generación de binarios (.elf / .exe)
#   GET  /passes            → Lista de passes disponibles
# Uso: python ui_compiler_v4.py
#      Abrir: http://localhost:5000
# ================================================================

import os
import sys

from flask import Flask, render_template, request, jsonify, send_file

# Asegurar que el directorio del script esté en el path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pipeline_v4 import run_pipeline
from ir_manual   import aplicar_passes, lista_passes_disponibles

app = Flask(__name__)

# Directorio base para archivos generados
DIRECTORIO_SALIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(DIRECTORIO_SALIDA, exist_ok=True)
ARCHIVO_BASE = os.path.join(DIRECTORIO_SALIDA, "programa")


# ──────────────────────────────────────────────────────────────
# RUTA PRINCIPAL
# ──────────────────────────────────────────────────────────────

@app.route('/')
def index():
    """Sirve la página principal del compilador."""
    return render_template('index_v4.html')


# ──────────────────────────────────────────────────────────────
# COMPILAR — Pipeline completo 8 fases
# ──────────────────────────────────────────────────────────────

@app.route('/compilar', methods=['POST'])
def compilar():
    """
    Recibe el código fuente y ejecuta el pipeline de 8 fases.

    Request body (JSON):
        {
            "codigo": "<source code>",
            "generar_binarios": false,
            "plataformas": ["linux"]
        }

    Response (JSON):
        {
            fases, tac, ir, ir_opt, consola, ir_out,
            binarios, stats_orig, stats_opt, ok
        }
    """
    datos = request.get_json(silent=True)
    if not datos or 'codigo' not in datos:
        return jsonify({"error": "No se recibió código fuente."}), 400

    codigo = datos.get('codigo', '')
    if not codigo.strip():
        return jsonify({"error": "El código fuente está vacío."}), 400

    generar_binarios = bool(datos.get('generar_binarios', False))
    plataformas      = datos.get('plataformas', ['linux'])

    resultado = run_pipeline(
        codigo,
        ARCHIVO_BASE,
        generar_binarios=generar_binarios,
        plataformas=plataformas
    )
    return jsonify(resultado)


# ──────────────────────────────────────────────────────────────
# OPTIMIZAR MANUAL — Passes individuales
# ──────────────────────────────────────────────────────────────

@app.route('/optimizar_manual', methods=['POST'])
def optimizar_manual():
    """
    Aplica un subconjunto de passes LLVM sobre el IR proporcionado.

    Request body (JSON):
        {
            "ir": "<llvm ir text>",
            "passes": ["mem2reg", "instcombine", "simplifycfg"]
        }

    Response (JSON):
        {
            ir_opt, diff, ok, tiempo_ms, error, passes_aplicados
        }
    """
    datos = request.get_json(silent=True)
    if not datos or 'ir' not in datos:
        return jsonify({"error": "No se recibió código IR."}), 400

    ir_texto = datos.get('ir', '')
    passes   = datos.get('passes', [])

    if not ir_texto.strip():
        return jsonify({"error": "El código IR está vacío."}), 400

    resultado = aplicar_passes(ir_texto, passes)
    return jsonify(resultado)


# ──────────────────────────────────────────────────────────────
# GENERAR BINARIO — Fase 8 independiente
# ──────────────────────────────────────────────────────────────

@app.route('/generar_binario', methods=['POST'])
def generar_binario():
    """
    Genera binarios (.elf y/o .exe) a partir del IR proporcionado.

    Request body (JSON):
        {
            "ir": "<llvm ir optimizado>",
            "plataformas": ["linux", "windows"]
        }

    Response (JSON):
        {
            binarios: { linux: "", windows: "" },
            errores:  [...],
            ok:       bool
        }
    """
    from pipeline_v4 import _generar_binario

    datos = request.get_json(silent=True)
    if not datos or 'ir' not in datos:
        return jsonify({"error": "No se recibió código IR."}), 400

    ir_texto    = datos.get('ir', '')
    plataformas = datos.get('plataformas', ['linux'])

    if not ir_texto.strip():
        return jsonify({"error": "El código IR está vacío."}), 400

    binarios = {}
    errores  = []

    for plataforma in plataformas:
        exito, ruta, err = _generar_binario(ir_texto, ARCHIVO_BASE, plataforma)
        if exito:
            binarios[plataforma] = os.path.basename(ruta)
        else:
            binarios[plataforma] = ""
            errores.append(f"[{plataforma}] {err}")

    return jsonify({
        "binarios": binarios,
        "errores":  errores,
        "ok":       len(errores) == 0
    })


# ──────────────────────────────────────────────────────────────
# DESCARGAR BINARIO
# ──────────────────────────────────────────────────────────────

@app.route('/descargar/<filename>')
def descargar(filename):
    """Permite descargar un binario generado."""
    ruta = os.path.join(DIRECTORIO_SALIDA, filename)
    if not os.path.exists(ruta):
        return jsonify({"error": "Archivo no encontrado."}), 404
    return send_file(ruta, as_attachment=True)


# ──────────────────────────────────────────────────────────────
# LISTA DE PASSES
# ──────────────────────────────────────────────────────────────

@app.route('/passes', methods=['GET'])
def get_passes():
    """Retorna la lista de passes LLVM disponibles para la UI."""
    return jsonify(lista_passes_disponibles())


# ──────────────────────────────────────────────────────────────
# PUNTO DE ENTRADA
# ──────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 60)
    print("  Compilador Interactivo v4 — Proyecto Final")
    print("  Abre tu navegador en: http://localhost:5000")
    print("=" * 60)
    app.run(debug=True, port=5000)