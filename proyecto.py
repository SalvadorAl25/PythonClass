fin = False
print("\n***********Calculadora************\nMenu\n1)Suma\n2)Resta\n3)Multiplicacion\n4)Divicion\n5)Salir\n")

while not(fin):
    opc = int(input("Opcion: "))
    if(opc==1):
        sum1=int(input("Sumando uno: "))
        sum2=int(input("Sumando dos: "))
        print("La suma es: ",sum1+sum2,"\n")
    elif(opc==2):
        minuendo = int(input("Minuendo: "))
        sustraendo = int(input("Sustraendo: "))
        print("La resta es: ",minuendo-sustraendo,"\n")
    elif(opc==3):
        multiplicando = int(input("Multiplcando: "))
        multiplicador = int(input("Multiplicador: "))
        print("La multiplicacion es: ", multiplicando*multiplicador,"\n")
    elif(opc==4):
        dividendo = int(input("Dividendo: "))
        divisor = int(input("Divisor: "))
        res = dividendo/divisor
        print("La divicion es: ",res,"\n")
    elif(opc==5):
        print("\nFin del programa\n")
        fin = True
