"""Ejercicio 06 — Una decisión sobre el plazo

Usa dias = 3 como número de días que faltan para devolver un libro. Si dias es mayor que 0, muestra "En plazo". Si es 0, "Vence hoy". Si es negativo, "Con retraso". Prueba también 0 y -2 cambiando la variable.

Comprueba: 3 produce En plazo, 0 produce Vence hoy y -2 produce Con retraso. Solo se ejecuta una rama.

Ampliación: Para un retraso, muestra además cuántos días han pasado desde el vencimiento.
"""



# Escribe tu solución debajo.

dias = -3 
if dias > 0:
    print("En plazo")
elif dias == 0:
    print("Vence hoy")
else:
    print("Con retraso")


nota = 5.5
if nota < 5:
    print("Suspenso")
elif nota < 6:
    print("Aprobado")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")

retraso = 0
if dias < 0:
    retraso = -dias
print(retraso)