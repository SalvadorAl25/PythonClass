print('Tarea 5: Problema 5')

c = float(input('Ingrese la cantidad de Capital: '))
r = float(input('Ingrese la tasa de interes: '))
t = float(input('Ingrese el tiempo: '))

m = ((1+r/100)**t)*c

print(f'\nEl monto es: {m:,.2f}')