def accederClave():
  """Intenta acceder a una clave inexistente en un diccionario, manejando KeyError."""
  diccionario = {"a": 1, "b": 2, "c": 3}
  clave = input("\n Ingrese la clave: ")
  try:
    valor = diccionario[clave]
    print(f"El valor de la clave '{clave}' es: {valor}")
  except KeyError:
    print(f"\n Error: La clave '{clave}' no existe en el diccionario.")

accederClave()