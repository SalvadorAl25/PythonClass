print('Tarea 14: Problema 7')

terminar = True
while terminar:
    n = int(input('Inserta un numero entrero del 1 al 4: '))
    if n >=1 & n <=4:
        if n == 1:
            print('Verano')
            terminar = False
        elif n == 2:
            print('Otoño')
            terminar = False
        elif n == 3:
            print('Invierno')
            terminar = False
        elif n == 4:
            print('Primavera')
            terminar = False