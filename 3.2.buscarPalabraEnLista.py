def buscarPalabra(*args):
    palabraBuscar = input("Ingrese la palabra que desea buscar: ")
    encontrada = True if palabraBuscar in args else False
    return f"La palabra '{palabraBuscar}' {'fue encontrada' if encontrada else 'no fue encontrada'} en la lista."

# Solicitar al usuario que ingrese la lista de palabras separadas por espacios
entradaUsuario = input("Ingrese una lista de palabras separadas por espacios: ").split()

# Llamar a la función buscar_palabra con las palabras ingresadas como argumentos
resultadoBusqueda = buscarPalabra(*entradaUsuario)

# Imprimir el resultado
print(resultadoBusqueda)