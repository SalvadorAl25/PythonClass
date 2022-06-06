print('Tarea 4: Problema 4')

print('Suma de los N primeros numeros enteros')

##Proceso
n = input('Inserte el valor de N: ')

if n.isnumeric():
    n = int(n)
    s = (n*(n+1))//2
    print(f'La suma es: {s}')
else:
    print(f'{n} no es un numero o no es positivo')