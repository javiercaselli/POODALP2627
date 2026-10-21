"""Ejercicio 05 — Dos objetos de una clase preparada

Guarda modelos_inicio.py en la misma carpeta. Escribe from modelos_inicio import Libro. Crea a = Libro("Dune") y b = Libro("1984"). Muestra a.titulo y los resultados de a.resumen() y b.resumen(). Explica qué comparten y qué distingue a los dos libros.

Comprueba: Los dos son de la clase Libro, pero sus títulos son distintos. Ambos comienzan disponibles.

Ampliación: Crea un tercer libro titulado "Fundación" y muestra su resumen.
"""

from modelos_inicio import Libro

# Escribe tu solución debajo.
a = Libro("Dune")
b = Libro("1984")
print(a.titulo)
print(a.resumen())
b.prestar()
print(b.resumen())

c = Libro("Fundación")
print(c.resumen())
