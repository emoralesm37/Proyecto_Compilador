# ================================================================
# custom_errors.py
# ErrorListeners personalizados para errores léxicos y sintácticos
# Sin cambios respecto al Proyecto 2 — reutilizado directamente
# ================================================================

from antlr4.error.ErrorListener import ErrorListener


class LexicoErrorListener(ErrorListener):
    """Captura errores léxicos: caracteres no reconocidos por la gramática."""

    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        simbolo = offendingSymbol.text if offendingSymbol else "desconocido"
        error = (
            f"[Error Léxico] Línea {line}, Columna {column}: "
            f"Símbolo no reconocido '{simbolo}'."
        )
        self.errores.append(error)

    def hay_errores(self):
        return len(self.errores) > 0

    def reporte(self):
        return "\n".join(self.errores)


class SintacticoErrorListener(ErrorListener):
    """Captura errores sintácticos: estructuras mal formadas."""

    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        simbolo = offendingSymbol.text if offendingSymbol else "<EOF>"

        if "missing" in msg and "at" in msg:
            esperado = msg.split("missing ")[1].split(" at")[0]
            error = (
                f"[Error Sintáctico] Línea {line}, Columna {column}: "
                f"Se esperaba {esperado} pero se encontró '{simbolo}'."
            )
        elif "extraneous input" in msg:
            error = (
                f"[Error Sintáctico] Línea {line}, Columna {column}: "
                f"Token inesperado '{simbolo}'."
            )
        elif "no viable alternative" in msg:
            error = (
                f"[Error Sintáctico] Línea {line}, Columna {column}: "
                f"Construcción inválida cerca de '{simbolo}'."
            )
        else:
            error = (
                f"[Error Sintáctico] Línea {line}, Columna {column}: {msg}"
            )

        self.errores.append(error)

    def hay_errores(self):
        return len(self.errores) > 0

    def reporte(self):
        return "\n".join(self.errores)
