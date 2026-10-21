"""Ejercicio 08 — Una lista que recorre el catálogo

Crea titulos = ["Dune", "1984"]. Añade "Fundación" con append. Recorre la lista con for y muestra un título por línea con su número, empezando por 1. Usa un contador que aumente en cada vuelta.

Comprueba: Aparecen tres títulos numerados 1, 2 y 3. La lista original sí cambia al llamar a append.

Ampliación: Cuenta cuántos títulos contienen la letra "a", ignorando mayúsculas.
"""

# Escribe tu solución debajo.
titulos = ["Dune", "1984"]
titulos.append("Fundación")
titulos.append("ESDLA")
index = 1
for titulo in titulos:
    print(f"{index}. {titulo}")
    index += 1

con_a = 0
for titulo in titulos:
    if "a" in titulo.lower():
        con_a += 1
print(f"Hay {con_a} títulos que contiene la letra 'a'")



