def funcion(*args):
    if len(args) < 2:
        print("Error: Se requieren al menos dos argumentos para esta función.")
        print() 
    else:
        print("Argumentos recibidos:", end=" ")   # Imprime sin salto de línea al final
        for i, arg in enumerate(args):
            print(arg, end=" ")         # Imprime cada argumento seguido de un espacio
        print()                         # Imprime un salto de línea al final de todos los argumentos
        print() 

# Ejemplos de llamadas a la función
print()
funcion("primer valor")
funcion("primer valor", "segundo valor")
funcion("primer valor", "segundo valor", "tercer valor")