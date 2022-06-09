print('Tarea 16: Problema 9')

n1 = int(input('Inserta un numero entero : '))
n2 = int(input('Inserta otro numero entero : '))
operador = input('Inserte un operador (+,-,*,/): ')

if operador == '+':
    print(f'El resultado de {n1} + {n2} es: {n1+n2}')
elif operador == '-':
    print(f'El resultado de {n1} - {n2} es: {n1-n2}')
elif operador == '*':
    print(f'El resultado de {n1} * {n2} es: {n1*n2}')
elif operador == '/':
    print(f'El resultado de {n1} / {n2} es: {n1/n2}')