from wsgiref.validate import validator


i=0
while i<10:
    print(i,end=" ")
    i=i+1

print("\n-----------------------------")

continuar = True
while continuar:
    valor = int(input("Inserta un numero entero superior a 100: "))
    if valor>100:
        continuar = False
print("Programa acabado")
