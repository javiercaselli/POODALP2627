"""Ejercicio 18 — La biblioteca de consola

Prepara una Biblioteca con L1 Dune y L2 1984. Implementa un menú: 1 listar, 2 prestar, 3 devolver y 0 salir. Reutiliza pedir_entero. Para préstamo o devolución solicita un código y distingue libro inexistente de operación rechazada. La interfaz muestra mensajes, pero cambia el estado llamando a métodos. Puedes copiar tus clases y funciones en el mismo archivo.

Comprueba: No debe fallar al introducir abc como opción. Rechaza prestar dos veces L1 y devolver dos veces L1. L9 se informa como inexistente. Al salir termina el bucle. Los datos se pierden al reiniciar: todavía no hay persistencia.

Ampliación: Añade la opción 4 para listar solo los disponibles.
"""
from e17 import pedir_entero

# Copia aquí tus clases de los ejercicios anteriores que se necesitan.
# Clase Libro
class Libro:
    def __init__(self, codigo, titulo: str, autor:str = "", fecha:str = ""):
            self.codigo = codigo
            self.titulo = titulo
            self.autor = autor
            self.fecha = fecha
            self.disponible = True

    def prestar(self) -> bool:
            if not self.disponible:
                return False
            else:
                self.disponible = False
                return True

    def devolver(self) -> bool:
          if self.disponible:
                return False
          self.disponible = True
          return True

    def resumen(self):
        if self.disponible:
            estado = "disponible"
        else:
            estado = "prestado"
        return f"{self.titulo}, {self.autor} - {self.fecha} [{estado}]"

# Clase biblioteca
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



# Escribe tu solución debajo.
if __name__ == "__main__":
     # Crea bibloteca
     biblioteca = Biblioteca()

     # Añade libros
     biblioteca.agregar(Libro("L1", "Dune"))
     biblioteca.agregar(Libro("L2", "1984"))

     # Menú
     opcion = -1
     while (opcion != 0):
          print("1. Listar")
          print("2. Prestar")
          print("3. Devolver")
          print("0. Salir")
          opcion = pedir_entero("Elija una opción: ")