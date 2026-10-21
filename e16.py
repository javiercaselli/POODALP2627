"""Ejercicio 16 — Una biblioteca contiene libros

Define Biblioteca con self.libros = [] en __init__. Añade buscar(codigo), agregar(libro) y prestar(codigo). agregar rechaza códigos repetidos y devuelve un booleano. prestar busca el objeto y delega en su método prestar. Si no lo encuentra, devuelve False. Un mismo título con códigos distintos sí se admite.

Comprueba: Agregar L1 funciona una vez. Agregar otro L1 falla sin reemplazar el anterior. Prestar L9 falla. Dos bibliotecas nuevas no comparten su lista.

Ampliación: Añade total_disponibles que devuelva cuántos libros disponibles tiene la biblioteca.
"""

# Copia aquí tus clases de los ejercicios anteriores que se necesitan.


# Escribe tu solución debajo.
from e13 import Libro


class Biblioteca:
    def __init__(self):
        self.libros = []

    def buscar(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro
        return None

    def agregar(self, libro):
        if self.buscar(libro.codigo) is not None:
            return False
        self.libros.append(libro)
        return True

    def prestar(self, codigo):
        libro = self.buscar(codigo)
        if libro is None:
            return False
        return libro.prestar()

    def total_disponibles(self):
        total = 0
        for libro in self.libros:
            if libro.disponible:
                total = total + 1
        return total

if __name__ == "__main__":
    biblioteca = Biblioteca()
    print(biblioteca.agregar(Libro("L1", "Dune")))
    print(biblioteca.agregar(Libro("L1", "1984")))
    print(biblioteca.prestar("L9"))
    print(biblioteca.prestar("L1"))

    biblioteca2 = Biblioteca()
    print(biblioteca2.agregar(Libro("L1", "Dune")))
    print(biblioteca2.agregar(Libro("L2", "1984")))
    print(biblioteca2.agregar(Libro("L3", "1984")))
    print(biblioteca2.prestar("L9"))

    print(biblioteca.buscar("L1").resumen())    
    print(biblioteca2.buscar("L1").resumen())

    print(biblioteca2.total_disponibles())
    biblioteca2.prestar("L2")
    print(biblioteca2.total_disponibles())