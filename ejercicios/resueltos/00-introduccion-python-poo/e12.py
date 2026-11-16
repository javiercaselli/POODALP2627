"""Ejercicio 12 — Nuestra primera clase

Crea tu propia clase Libro. Su inicializador recibe codigo y titulo, guarda ambos en self y establece disponible = True. Crea L1 con Dune y L2 con 1984. Muestra sus títulos. En esta versión añadimos un código para distinguir ejemplares incluso si comparten título.

Comprueba: L1 y L2 tienen códigos y títulos independientes. Ambos empiezan disponibles. Cambiar el título del primero no cambia el segundo.

Ampliación: Añade autor al inicializador y crea dos objetos con autores diferentes.
"""



# Escribe tu solución debajo.
class Libro:
    def __init__(self, codigo, titulo: str, autor: str):
            self.codigo = codigo
            self.titulo = titulo
            self.autor = autor
            self.disponible = True

if __name__ == "__main__":
      l1 = Libro("L1", "Dune", "Frank Herbert")
      l2 = Libro("L2", "1984", "George Horwell")

