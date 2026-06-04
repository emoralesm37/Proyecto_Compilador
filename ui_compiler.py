# ================================================================
# ui_compiler.py
# Interfaz de Compilación Interactiva — Proyecto 3
# Servidor Flask que expone la UI web del compilador
# Uso: python ui_compiler.py
#      Luego abrir: http://localhost:5000
# ================================================================

import os
import sys
from flask import Flask, render_template, request, jsonify

# Asegurar que el directorio actual esté en el path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pipeline_back import run_pipeline

app = Flask(__name__)


# ──────────────────────────────────────────────────────────────
# RUTAS
# ──────────────────────────────────────────────────────────────

@app.route('/')
def index():
    """Sirve la página principal del compilador."""
    return render_template('index.html')


@app.route('/compilar', methods=['POST'])
def compilar():
    """
    Recibe el código fuente como JSON y ejecuta el pipeline.
    Request body: { "codigo": "<source code>" }
    Response:     { fases, tac, ir, consola, ir_out, ok }
    """
    datos = request.get_json(silent=True)
    if not datos or 'codigo' not in datos:
        return jsonify({"error": "No se recibió código fuente."}), 400

    codigo = datos['codigo']
    if not codigo.strip():
        return jsonify({"error": "El código fuente está vacío."}), 400

    # Directorio de salida para .tac y .ll
    directorio_salida = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "output")
    os.makedirs(directorio_salida, exist_ok=True)
    archivo_base = os.path.join(directorio_salida, "programa")

    resultado = run_pipeline(codigo, archivo_base)
    return jsonify(resultado)


# ──────────────────────────────────────────────────────────────
# PUNTO DE ENTRADA
# ──────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 55)
    print("  Compilador Interactivo v3 — Proyecto 3")
    print("  Abre tu navegador en: http://localhost:5000")
    print("=" * 55)
    app.run(debug=True, port=5000)
