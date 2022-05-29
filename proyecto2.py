def Suma():
    sum1=int(input("Sumando uno: "))
    sum2=int(input("Sumando dos: "))
    print("La suma es: ",sum1+sum2,"\n")

def Resta():
    minuendo = int(input("Minuendo: "))
    sustraendo = int(input("Sustraendo: "))
    print("La resta es: ",minuendo-sustraendo,"\n")

def Multiplicacion():
    multiplicando = int(input("Multiplcando: "))
    multiplicador = int(input("Multiplicador: "))
    print("La multiplicacion es: ", multiplicando*multiplicador,"\n")

def Divicion():
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    res = dividendo/divisor
    print("La divicion es: ",res,"\n")

def Titulo():
    print("***********Calculadora************\nMenu\n1)Suma\n2)Resta\n3)Multiplicacion\n4)Divicion\n5)Salir\n")

fin = False
Titulo()
while not(fin):
    opc = int(input("Opcion: "))
    if(opc==1):
        Suma()
        Titulo()
    elif(opc==2):
        Resta()
        Titulo()
    elif(opc==3):
        Multiplicacion()
        Titulo()
    elif(opc==4):
        Divicion()
        Titulo()
    elif(opc==5):
        print("\nFin del programa\n")
        fin = True