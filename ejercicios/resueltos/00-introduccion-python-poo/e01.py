"""Ejercicio 01 — La ficha de un libro

Crea titulo = "Dune", paginas = 412 y disponible = True. Muestra cada valor y su tipo con print y type. Cambia solo el título a "1984" y vuelve a mostrarlo. Antes de ejecutar, predice qué línea cambiará.

Comprueba: Los tipos son str, int y bool. El cambio del título no modifica las páginas ni la disponibilidad.

Ampliación: Añade autor = "Frank Herbert" y comprueba su tipo.
"""



# Escribe tu solución debajo.
titulo = "Dune"
paginas = 412
disponible = True
print(titulo, type(titulo))
print(paginas, type(paginas))
print(disponible, type(disponible))

titulo = "1984"
print(titulo, type(titulo))

titulo = 1984
print(titulo, type(titulo))
