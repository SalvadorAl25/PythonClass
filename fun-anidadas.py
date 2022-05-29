def SumarRestar(param1,param2):
    return Sumar(param1, param2), Restar(param1,param2)

def Sumar(sum1, sum2):
    return sum1 + sum2

def Restar(num1, num2):
    return num1 - num2

n1 = int(input("Inserta un numero: "))
n2 = int(input("Inserta otro numero: "))
resSum, resResta = SumarRestar(n1, n2)
print("El resultado de la suma es: ", resSum)
print("El resultado de la resta es: ", resResta)