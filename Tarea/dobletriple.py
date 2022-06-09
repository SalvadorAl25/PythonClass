print('Tarea 11: Problema 4')

n = int(input('Inserta un numero entero: '))

if n % 2 == 0:
    n = n * 3
    print(f'El numero insertado es Par, {n}')
else:
    n = n * 2
    print(f'El numero insertado es Impar, {n}')
