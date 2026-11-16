from .modelos import Material


def registrar_prestamo(material: Material) -> str:
    resultado = "aceptado" if material.prestar() else "rechazado"
    return f"{material.ficha()} · préstamo {resultado}"