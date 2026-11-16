"""Ejercicio 07 — El primer préstamo

Crea un Libro de la clase preparada. Llama a prestar dentro de un if. Muestra "Préstamo realizado" si devuelve True y "No disponible" en caso contrario. Repite el intento sobre el mismo objeto. Muestra su resumen después de cada intento.

Comprueba: El primer intento tiene éxito y el segundo falla. El libro termina prestado. El método devuelve un booleano y también cambia su estado cuando puede prestar.

Ampliación: Crea otro ejemplar con el mismo título y comprueba que sigue disponible.
"""
from modelos_inicio import Libro

# Escribe tu solución debajo.
libro = Libro("Dune")
if libro.prestar():
    print("Préstamo realizado")
else:
    print("No disponible")
print(libro.resumen())

if libro.prestar():
    print("Préstamo realizado")
else:
    print("No disponible")
print(libro.resumen())

otroLibro = Libro("Dune")
print(otroLibro.resumen())
