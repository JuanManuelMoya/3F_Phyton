# Solicitar al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Calcular el mayor usando el operador ternario
mayor = num1 if num1 > num2 else num2

# Imprimir el resultado
print(f"El mayor de los dos números es: {mayor}")