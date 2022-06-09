print('Tarea 13: Problema 6')

n1 = int(input('Inserta un numero entero: '))
n2 = int(input('Inserta otro numero entero: '))
n3 = int(input('Inserta otra vez otro numero entero: '))

if n1 > n2 & n1 > n3:
    if n2 > n3:
        may = n1
        med = n2
        men = n3
    else:
        may = n1
        med = n3
        men = n2
elif n2 > n1 & n2 > n3:
    if n1 > n3:
        may = n2
        med = n1
        men = n3
    else:
        may = n1
        med = n3
        men = n2
elif n3 > n1 & n3 > n2:
    if n1 > n2:
        may = n3
        med = n1
        men = n2
    else:
        may = n1
        med = n3
        men = n2

print(f'Numeros ordenados: {may}, {med}, {men}. y la suma de ellos es: {may+med+men}')