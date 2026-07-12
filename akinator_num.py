print("======================================")
print(" - Bienvenido al Akinator Numérico - ")
print("======================================")
print("Piensa en un número del 1 al 100 en tu mente.")
print("Yo intentaré adivinarlo. Solo responde con:")
print(" '>' si tu número es mayor.")
print(" '<' si tu número es menor.")
print(" '=' si adiviné tu número.")
print("========================================")

input("Cuando estés listo, presiona Enter para empezar...")

inferior = 1
superior = 100
adivinado = false
intentos_totales = 0

while not adivinado:
  intento = (inferior + superior) // 2
  intentos_totales += 1
  print(f"\n¿Tu numero es el {intento}?")
  respuesta = input("Respuesta (>, <, =): ").strip()
  
  if respuesta == "=":
    print(f"Gane! Lo adivine en solo {intentos_totales} intentos, la maquina domina!")
    adivinado = True
  elif respuesta == ">":
    inferior = intento + 1
  elif respuesta == "<":
    superior = intento - 1
  else:
    print("X, respuesta no válida. Por favor usa '>', '<' o '='.")
    intentos_totales -=1

    
