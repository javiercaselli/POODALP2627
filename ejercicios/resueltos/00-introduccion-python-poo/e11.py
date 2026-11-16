T"""Ejercicio 11 — Una función recibe un objeto

Define etiqueta(libro). Devuelve "Dune [disponible]" o "Dune [prestado]" según el título y estado del objeto recibido. Crea un Libro preparado y muestra su etiqueta antes y después de prestarlo. La función etiqueta no debe modificarlo.

Comprueba: La etiqueta cambia después del préstamo. El objeto mantiene el mismo título. Consultarlo no lo presta.

Ampliación: Define prestar_y_etiquetar(libro), que intente prestarlo y devuelva su etiqueta. Explica qué función consulta y cuál modifica.
"""



# Escribe tu solución debajo.
from modelos_inicio import Libro


def etiqueta(libro: Libro) -> str:
    if libro.disponible:
        estado = "disponible"
    else:
        estado = "prestado"
    return f"{libro.titulo}, {libro.autor} - {libro.fecha} [{estado}]"

def prestar_y_etiquetar(libro: Libro) -> str:
    libro.prestar()
    return etiqueta(libro)

if __name__ == "__main__":
    libro = Libro("Dune", 1965, "Frank Herbert")
    print(etiqueta(libro))
    libro.prestar()
    print(etiqueta(libro))

    libro2 = Libro("ESDLA", 1967, "JRR Tolkien")
    print(etiqueta(libro2))
    print(prestar_y_etiquetar(libro2))
