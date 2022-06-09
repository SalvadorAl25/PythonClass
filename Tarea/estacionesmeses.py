print('Tarea 17: Problema 10')


n = int(input('Inserta el numero de mes: '))
if n < 4:
    print('Es Verano')
elif n < 7:
    if n > 3:
        print('Es Otoño')
elif n < 10:
    if n > 6:
        print('Es Invierno')
elif n < 13:
    if n > 9:
        print('Es Primavera')