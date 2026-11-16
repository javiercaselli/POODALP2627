from biblioteca.modelos import Libro, Revista
from biblioteca.prestamos import registrar_prestamo


def main():
    for material in [Libro("Dune"), Revista("Ciencia hoy", 7)]:
        print(registrar_prestamo(material))
        print(registrar_prestamo(material))

if __name__ == "__main__":
    main()