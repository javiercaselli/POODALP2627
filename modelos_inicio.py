class Libro:
    """Modelo preparado para aprender a usar objetos."""
    def __init__(self, titulo, fecha=2026, autor=None):
        self.titulo = titulo
        self.disponible = True
        self.fecha = fecha
        self.autor = autor


    def prestar(self):
        if not self.disponible:
            return False
        self.disponible = False
        return True

    def resumen(self):
        if self.disponible:
            estado = "disponible"
        else:
            estado = "prestado"
        return f"{self.titulo}: {estado}"
