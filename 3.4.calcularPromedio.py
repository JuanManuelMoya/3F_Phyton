def calcularPromedio(*args):
    cantidad = len(args)
    promedio = sum(args) / cantidad if cantidad > 0 else 0.0
    return promedio

# Solicitar al usuario que ingrese los números separados por espacios
entradaUsuario = input("Ingrese una lista de números separados por espacios: ").split()

# Convertir las cadenas ingresadas a números (manejar posibles errores)
numeros = []
for item in entradaUsuario:
    try:
        numeros.append(float(item))
    except ValueError:
        print(f"Advertencia: '{item}' no es un número válido y será ignorado.")

# Calcular el promedio utilizando la función con *args
promedioCalculado = calcularPromedio(*numeros)

# Imprimir el resultado
print(f"El promedio de los números ingresados es: {promedioCalculado}")