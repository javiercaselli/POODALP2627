"""Ejercicio 14 — Dos nombres o dos objetos

Crea a = Libro("L1", "Dune"), b = a y c = Libro("L2", "Dune"). Antes de ejecutar b.prestar(), predice qué ocurrirá con a.disponible y c.disponible. Ejecuta y muestra a is b y a is c. is comprueba si dos referencias apuntan al mismo objeto.

Comprueba: a y b nombran el mismo objeto, que queda prestado. c es otro y sigue disponible. a is b es True y a is c es False.

Ampliación: Crea dos listas, copia = lista y separada = lista.copy(). Añade un elemento a copia y explica cuál de las dos listas cambia. La copia es superficial.
"""

# Copia aquí tus clases de los ejercicios anteriores que se necesitan.


# Escribe tu solución debajo.
from e13 import Libro

if __name__ == "__main__":
    a = Libro("L1", "Dune")
    b = a
    d = 7
    e = d
    c = Libro("L2", "Dune")
    b.prestar()
    print (a.disponible, c.disponible)
    print (a is b, a is c)
    d = d + 1
    print (d, e)

    lista = [a]
    copia = lista
    clon = lista.copy()
    copia.append(c)
    print (len(lista), len(clon))