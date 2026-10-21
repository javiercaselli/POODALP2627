"""Ejercicio 09 — Un menú que se repite

Pide una opción de texto mientras no sea "0". "1" muestra "Catálogo". "0" muestra "Hasta luego" y termina. Cualquier otro texto muestra "Opción no válida". No conviertas la entrada a número.

Comprueba: Con la secuencia 7, 1, 0 hay un aviso, un Catálogo y una despedida. El programa termina tras 0.

Ampliación: Cuenta cuántas veces se ha elegido la opción 1 y muéstralo al salir.
"""



# Escribe tu solución debajo.
opcion = ""
veces_op1 = 0
while opcion != "0":
    opcion = input("1. Catálogo / 0. Salir: ")
    if opcion == "1":
        print("Catálogo")
        veces_op1 += 1
    elif opcion == "0":
        print("Hasta luego")
    else:
        print("Opción no válida")

print(f"Se han realizado {veces_op1} consultas al catálogo")

