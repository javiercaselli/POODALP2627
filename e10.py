"""Ejercicio 10 — Una función que calcula

Define dias_restantes(plazo, transcurridos). Debe devolver la resta, sin imprimirla ni cambiar los argumentos. Llama a la función y muestra el resultado desde fuera. Prueba (14, 4), (14, 14) y (14, 17).
 
Comprueba: Los resultados son 10, 0 y -3. return entrega un valor que se puede guardar. print solo lo muestra.

Ampliación: Define estado_plazo(plazo, transcurridos), reutilizando dias_restantes, que devuelva En plazo, Vence hoy o Con retraso.
"""



# Escribe tu solución debajo.
def dias_restantes(dias_plazo:int, dias_transcurridos:int) -> int:
    return dias_plazo - dias_transcurridos

def estado_plazo(dias_plazo: int, dias_transcurridos: int) -> str:
    dias = dias_restantes(dias_plazo, dias_transcurridos)

    if dias > 0:
        return "En plazo"
    elif dias == 0:
        return "Vence hoy"
    else:
        return "Con retraso"


if __name__ == "__main__":
    print(dias_restantes(14, 4))
    print(dias_restantes(14, 14))
    print(dias_restantes(14, 17))

    print(estado_plazo(14, 4))
    print(estado_plazo(14, 14))
    print(estado_plazo(14, 17))


