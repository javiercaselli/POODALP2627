"""Ejercicio 15 — Buscar entre objetos

Crea una lista con L1 Dune y L2 1984. Define buscar(libros, codigo): devuelve el objeto cuyo código coincide o None si no existe. Prueba L1 y L9. Solo llama a prestar cuando el resultado no sea None.

Comprueba: Buscar L1 devuelve el propio objeto almacenado. Buscar L9 devuelve None. Prestar el resultado de L1 modifica el objeto de la lista.

Ampliación: Define disponibles(libros) que construya y devuelva una lista con los libros disponibles.
"""

# Copia aquí tus clases de los ejercicios anteriores que se necesitan.


# Escribe tu solución debajo.
from e13 import Libro

def buscar(libros:Libro, codigo:str):
    for libro in libros:
        if libro.codigo == codigo:
            return libro
    return None


if __name__ == "__main__":
    libros = [Libro("L1", "Dune"), Libro("L2", "1984")]
    encontrado = buscar(libros, "L1")
    if encontrado is not None:
        encontrado.prestar()
    print(libros[0].disponible, libros[1].disponible)
    print(buscar(libros, "L9"))
