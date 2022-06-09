print('Tarea 11: Problema 4')

n1 = int(input('Inserta el 1er numero entero: '))

n2 = int(input('Inserta el 2do numero entero: '))

n3 = int(input('Inserta el 3er numero entero: '))

if n1>n2:
    if n1 > n3:
        print(f'Numero {n1} es el mayor')
    else:
        print(f'Numero {n3} es el mayor')
else:
    if n2 > n3:
        print(f'Numero {n2} es el mayor')
    else:
        print(f'Numero {n3} es el mayor')