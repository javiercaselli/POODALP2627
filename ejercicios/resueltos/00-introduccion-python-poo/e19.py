"""Ejercicio 19 — Guardar y recuperar el catálogo

Extensión opcional hacia RA3. Define guardar(biblioteca, ruta) y cargar(ruta). Guarda una lista de diccionarios con codigo, titulo y disponible. Al cargar, crea una nueva Biblioteca y nuevos Libro, recuperando el estado mediante prestar si corresponde. En este ejercicio el JSON tiene el formato esperado y códigos únicos. Préstale L1, guarda, carga y comprueba su estado.

Comprueba: La nueva biblioteca conserva títulos, códigos y disponibilidad, pero contiene instancias nuevas. Un título con tildes se conserva. JSON almacena datos, no los métodos del objeto.

Ampliación: Si el fichero no existe, devuelve una biblioteca vacía. Un JSON dañado debe seguir mostrando su error, sin ocultarlo.
"""
import json


# Reutiliza tus clases Libro y Biblioteca del ejercicio 16.
# Clase Libro
class Libro:
    def __init__(self, codigo, titulo: str, autor:str = "", fecha:str = ""):
            self.codigo = codigo
            self.titulo = titulo
            self.autor = autor
            self.fecha = fecha
            self.disponible = True

    def prestar(self) -> bool:
            if not self.disponible:
                return False
            else:
                self.disponible = False
                return True

    def devolver(self) -> bool:
          if self.disponible:
                return False
          self.disponible = True
          return True

    def resumen(self):
        if self.disponible:
            estado = "disponible"
        else:
            estado = "prestado"
        return f"{self.codigo}|{self.titulo}, {self.autor} - {self.fecha} [{estado}]"

# Clase biblioteca
class Biblioteca:
    def __init__(self):
        self.libros:list[Libro] = []

    def buscar(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro
        return None

    def agregar(self, libro):
        if self.buscar(libro.codigo) is not None:
            return False
        self.libros.append(libro)
        return True

    def prestar(self, codigo):
        libro = self.buscar(codigo)
        if libro is None:
            return False
        return libro.prestar()

    def total_disponibles(self):
        total = 0
        for libro in self.libros:
            if libro.disponible:
                total = total + 1
        return total


# Escribe tu solución debajo.
def guardar(biblioteca: Biblioteca, ruta):
    datos = []
    for libro in biblioteca.libros:
        datos.append({"codigo": libro.codigo,
                      "titulo": libro.titulo,
                      "autor": libro.autor,
                      "fecha": libro.fecha,
                      "disponible": libro.disponible})
    with open(ruta, "w", encoding="utf-8") as archivo:
         json.dump(datos, archivo, ensure_ascii=False)

def cargar(ruta):
    with open(ruta, encoding="utf-8") as archivo:
         datos = json.load(archivo)
    biblioteca = Biblioteca()
    for dato in datos:
        libro = Libro(dato["codigo"], dato["titulo"], dato["autor"], dato["fecha"])
        if not dato["disponible"]:
             libro.prestar()
        biblioteca.agregar(libro)
    return biblioteca

if __name__ == "__main__":
    b = Biblioteca()
    b.agregar(Libro("L1", "Fundación"))
    b.prestar("L1")
    b.agregar(Libro("L2", "1984"))
    guardar(b, "catalago_e19.json")
    recuperada = cargar("catalago_e19.json")
    print(recuperada.buscar("L2").resumen())