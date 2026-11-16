class Material:
    def __init__(self, titulo):
        self.titulo = titulo
        self._disponible = True

    @property
    def disponible(self):
        return self._disponible

    def prestar(self):
        if not self.disponible:
            return False
        self._disponible = False
        return True

    def devolver(self):
        if self.disponible:
            return False
        self._disponible = True
        return True

    def ficha(self):
        return self.titulo

class Libro(Material):
    pass

class Revista(Material):
    def __init__(self, titulo, numero):
        super().__init__(titulo)
        self.numero = numero

    def ficha(self):
        return f"{super().ficha()} · n.º {self.numero}"

class Catalogo:
    def __init__(self):
        self._materiales = []

    def agregar(self, material):
        self._materiales.append(material)

    def fichas(self):
        return [material.ficha() for material in self._materiales]

catalogo = Catalogo()
libro = Libro("Dune")
assert libro.prestar()
assert libro.devolver()
catalogo.agregar(libro)
catalogo.agregar(Revista("Ciencia hoy", 7))
print(catalogo.fichas())  # ['Dune', 'Ciencia hoy · n.º 7']