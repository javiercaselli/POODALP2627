"""Ejercicio 02 — Un cálculo de existencias

Una biblioteca tiene 12 ejemplares y ha prestado 5. Calcula cuántos quedan y qué porcentaje representan. Guarda ambos resultados y muéstralos con un texto. Usa una cadena f para incluir valores, por ejemplo f"Quedan {restantes}". Supón que el total es positivo.

Comprueba: Quedan 7 ejemplares. El porcentaje es aproximadamente 58,33. Si prestados vale 0, quedan 12 y el porcentaje es 100.

Ampliación: Calcula cuántas cajas de 5 ejemplares se llenan con los 12 y cuántos sobran.
"""



# Escribe tu solución debajo.
total = 13
prestados = 5
restantes = total - prestados
porcentaje = (restantes / total) * 100
print (f"Quedan {restantes} ejemplares")
print (f"Porcentaje: {porcentaje:.2f}")

capacidad_caja = 5
cajas_llenas = total // capacidad_caja
ejemplares_sobrantes = total % capacidad_caja
print (cajas_llenas, ejemplares_sobrantes)