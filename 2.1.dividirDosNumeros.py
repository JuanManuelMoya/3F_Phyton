def dividirDosNumeros():
  """Pide al usuario dos números y los divide, 
  manejando error de dividir por ceroZeroDivisionError."""
  try:
    numero1 = input("\n Ingrese el primer número (dividendo): ")
    num1 = float(numero1)  # Convertir la entrada a un número flotante

    numero2 = input(" Ingrese el segundo número (divisor): ")
    num2 = float(numero2)  # Convertir la entrada a un número flotante

    resultado = num1 / num2
    print(f"\n El resultado de {num1} dividido por {num2} es: {resultado:.2f}\n")

  except ZeroDivisionError:
    print("Error: No se puede dividir por cero.\n")

# Llamada a la función para ejecutar el programa
dividirDosNumeros()
