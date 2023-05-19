# Solicitar al usuario ingresar tres números
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

# Encontrar el número mayor
mayor = n1
if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3

# Encontrar el número menor
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

# Encontrar el número intermedio
intermedio = n1 + n2 + n3 - (mayor + menor)

# Imprimir los números en orden ascendente
print("Los números ordenados en forma ascendente son:", menor, intermedio, mayor)
