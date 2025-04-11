def sumarNumeroMasCadena():
  """Sumar un número y una cadena, manejando TypeError."""
  try:
    numero = input("\n Ingrese un numero ")
    numero = float(numero)  # Convertir la entrada a un número flotante
    cadena = input("\n Ingrese una cadena ")
    cadena = float(cadena)  # Convertir la entrada a un número flotante
    resultado = numero + cadena
    print(f" El resultado es: {resultado:.2f}\n")
  except TypeError:
    print(" Error: No se puede sumar un número y una cadena.\n")

sumarNumeroMasCadena()
