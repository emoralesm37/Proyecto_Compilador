# ================================================================
# Tabla_de_simbolos.py
# Tabla de Símbolos — Pila de Tablas Hash (Stack of Hash Tables)
# Cada ámbito (scope) es un dict de Python (tabla hash)
# Índice 0 = ámbito global; push al entrar, pop al salir
# ================================================================


class TablaSimbolos:

    def __init__(self):
        # Pila de tablas hash: index 0 = global scope
        self.pilaScopes: list[dict] = [{}]

    # ──────────────────────────────────────────────────────────
    # GESTIÓN DE SCOPES
    # ──────────────────────────────────────────────────────────

    def push_scope(self):
        """Entra a un nuevo ámbito (función, ciclo, bloque)."""
        self.pilaScopes.append({})

    def pop_scope(self):
        """Sale del ámbito actual."""
        if len(self.pilaScopes) <= 1:
            raise Exception("[Tabla de Símbolos] No se puede eliminar el ámbito global.")
        return self.pilaScopes.pop()

    def profundidad(self):
        """Retorna el nivel de anidamiento actual."""
        return len(self.pilaScopes)

    # ──────────────────────────────────────────────────────────
    # VARIABLES
    # ──────────────────────────────────────────────────────────

    def declarar_variable(self, nombre: str, tipo: str, valor=None,
                          linea=None, columna=None):
        """
        Declara una variable en el ámbito ACTUAL (tabla hash del tope).
        Error si ya existe en ese mismo ámbito (shadowing controlado).
        """
        scope_actual = self.pilaScopes[-1]

        if nombre in scope_actual:
            loc = f"Línea {linea}, Columna {columna}: " if linea else ""
            raise Exception(
                f"[Error Semántico] {loc}"
                f"Variable '{nombre}' ya fue declarada en este ámbito."
            )

        scope_actual[nombre] = {
            'categoria': 'variable',
            'tipo':      tipo,
            'valor':     valor
        }

    def buscar(self, nombre: str):
        """
        Busca una variable desde el ámbito más interno al más externo.
        Respeta shadowing: retorna la primera coincidencia (más interna).
        Retorna None si no se encuentra.
        """
        for scope in reversed(self.pilaScopes):
            if nombre in scope:
                return scope[nombre]
        return None

    def buscar_scope_actual(self, nombre: str):
        """Busca SOLO en el ámbito actual (para detectar redeclaraciones)."""
        return self.pilaScopes[-1].get(nombre, None)

    def asignar(self, nombre: str, valor, linea=None, columna=None):
        """Actualiza el valor de una variable ya declarada."""
        for scope in reversed(self.pilaScopes):
            if nombre in scope:
                scope[nombre]['valor'] = valor
                return
        loc = f"Línea {linea}, Columna {columna}: " if linea else ""
        raise Exception(
            f"[Error Semántico] {loc}Variable '{nombre}' no fue declarada."
        )

    def obtener_valor(self, nombre: str):
        simbolo = self.buscar(nombre)
        return simbolo['valor'] if simbolo else None

    def obtener_tipo(self, nombre: str):
        simbolo = self.buscar(nombre)
        return simbolo['tipo'] if simbolo else None

    # ──────────────────────────────────────────────────────────
    # FUNCIONES (siempre en ámbito global — índice 0)
    # ──────────────────────────────────────────────────────────

    def declarar_funcion(self, nombre: str, tipo_retorno: str,
                         parametros: list, linea=None, columna=None):
        """
        Registra una función en el ámbito global.
        parametros: lista de tuplas (tipo, nombre)
        """
        scope_global = self.pilaScopes[0]

        if nombre in scope_global:
            loc = f"Línea {linea}, Columna {columna}: " if linea else ""
            raise Exception(
                f"[Error Semántico] {loc}Función '{nombre}' ya fue declarada."
            )

        scope_global[nombre] = {
            'categoria':     'funcion',
            'tipo':          'function',
            'tipo_retorno':  tipo_retorno,
            'parametros':    parametros,   # [(tipo, nombre), ...]
            'valor':         None
        }

    def buscar_funcion(self, nombre: str):
        """Busca una función SOLO en el ámbito global."""
        entrada = self.pilaScopes[0].get(nombre, None)
        if entrada and entrada.get('categoria') == 'funcion':
            return entrada
        return None

    # ──────────────────────────────────────────────────────────
    # UTILIDADES
    # ──────────────────────────────────────────────────────────

    def imprimir(self):
        """Imprime el estado completo de la tabla para depuración."""
        print("\n" + "─" * 55)
        print(" Tabla de Símbolos — Estado Final ")
        print("─" * 55)
        for i, scope in enumerate(self.pilaScopes):
            nombre_scope = "Global" if i == 0 else f"Scope nivel {i}"
            print(f"\n  [{nombre_scope}]")
            if not scope:
                print("    (vacío)")
            for nombre, info in scope.items():
                if info['categoria'] == 'funcion':
                    params = ", ".join(
                        f"{t} {n}" for t, n in info['parametros']
                    )
                    print(f"    {info['tipo_retorno']} {nombre}({params})")
                else:
                    print(
                        f"    {info['tipo']:8} {nombre:12} = {info['valor']}"
                    )
        print("─" * 55)