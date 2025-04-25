def determinarParidad(numero):
  resultado = "Par" if numero % 2 == 0 else "Impar"
  return resultado

while True:
  try:
    entrada = input("Ingrese un número entero (o 'salir' para terminar): ").lower()
    if entrada == 'salir':
      break

    num = int(entrada)
    resultado = determinarParidad(num)
    print(f"El número {num} es {resultado}.")
  except ValueError:
    print("Por favor, ingrese un número entero válido o 'salir'.")

print("Programa terminado.")
