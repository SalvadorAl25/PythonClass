numeros = []

for i in range(6):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

numero_mayor = max(numeros)
numero_menor = min(numeros)

print("El número mayor es:", numero_mayor)
print("El número menor es:", numero_menor)
