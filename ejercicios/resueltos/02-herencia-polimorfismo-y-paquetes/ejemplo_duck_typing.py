class Mapa:
    def ficha(self):
        return "Mapa de caminos"

class Audio:
    def ficha(self):
        return "Audio · Recorrido por el centro"

def imprimir_informe(materiales):
    for material in materiales:
        print(material.ficha())

imprimir_informe([Mapa(), Audio()])
# Mapa de caminos
# Audio · Recorrido por el centro