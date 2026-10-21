"""Ejercicio 13 — Métodos que cumplen una regla

Añade prestar y devolver a tu clase. prestar devuelve True y cambia disponible a False solo si estaba disponible. En caso contrario devuelve False y conserva el estado. devolver hace la operación inversa y también informa con un booleano. Usa la clase en cuatro llamadas: prestar, prestar, devolver, devolver.

Comprueba: Las llamadas devuelven True, False, True, False. El estado final es disponible. Un intento rechazado no altera el objeto.

Ampliación: Añade resumen, equivalente a etiqueta del ejercicio 11 pero sin parámetro libro: usa self.
"""



# Escribe tu solución debajo.
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
        return f"{self.titulo}, {self.autor} - {self.fecha} [{estado}]"
          
if __name__ == "__main__":
     libro = Libro("L1", "Dune", "Frank Herbert", "1965")
     print(libro.prestar())
     print(libro.prestar())
     print(libro.devolver())
     print(libro.devolver())
