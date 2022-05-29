def Saludar():
    print("Hola Time of Software!")
Saludar()

print("-----------------Es Mayor Que Zero------------------------")

def EsMayorQueCero(param):
    if param > 0:
        print(param, "Es mayor que cero")
    else:
        print(param, "No es mayor que cero")

numero = int(input("Introduce un numero: "))
EsMayorQueCero(numero)

print("---------------------Suma--------------------------------")

def Suma(param1, param2):
    return param1+param2
num1 = int(input("Inserta primer sumando: "))
num2 = int(input("Inserta segundo sumando: "))
res = Suma(num1, num2)
print("El resultado de la suma es: ",res)

print("---------------------Suma incremento valores--------------------------------")

def Sumar(*valores):
    res = 0
    for item in valores:
        res = res + item
    return res
res = Sumar(23,56,3,89,78,455)
print("El resultado de la suma es: ",res)