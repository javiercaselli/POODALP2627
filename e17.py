"""Ejercicio 17 — Una entrada incorrecta no termina el programa

Define pedir_entero(mensaje). Repite input hasta recibir un entero mayor o igual que cero. Si int falla, muestra "Escribe un entero". Si el valor es negativo, muestra "No puede ser negativo". Si es válido, devuélvelo. Introduce abc, -2, 0.

Comprueba: Hay dos avisos y la función devuelve 0. Una entrada vacía o "2.5" también debe volver a pedir el dato.

Ampliación: Define pedir_opcion(mensaje, maximo) que reutilice pedir_entero y rechace valores superiores al máximo.
"""

# Copia aquí tus clases de los ejercicios anteriores que se necesitan.


# Escribe tu solución debajo.
def pedir_entero(mensaje):
    while True:
        texto = input(mensaje)
        try:
            valor = int(texto)
        except ValueError:
            print("Escribe un entero")
            continue
        if valor < 0:
            print("No puede ser negativo")
        else:
            return valor

def pedir_opcion(mensaje, maximo):
    while True:
        numero = pedir_entero(mensaje)
        if numero <= maximo:
            return numero
        print("Opción fuera de rango")

if __name__ == "__main__":
    print(pedir_entero("Introduzca un número: "))