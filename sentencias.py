cadena = "En un lugar de la mancha..."
if "lugar" in cadena:
    print("¡Encontrado!")
else:
    print("No encontrado...")

if cadena.startswith('E'):
    print("¡Empieza por E!")
else:
    print("¡No empieza con E")
if cadena.endswith('p'):
    print("¡Termina por p!")
else:
    print("¡No termina por p!")

print("--------------------")

numero1 = int(input("Inserte el primer numero: "))
numero2 = int(input("Inserte el segundo numero: "))

if numero1>numero2:
    print("El primer numero es mayor que el segundo")
elif numero1 == numero2:
    print("Ambos numeros son iguales")
else:
    print("El primer numero es menor que el segundo")
    