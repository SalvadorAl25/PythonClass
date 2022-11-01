n = int(input('Cantidad de Numeros: '))
cont = 0
i=1
while i < n:
    if i % 5 == 0:
        cont += 1
    i += 1
print(f'entre los {n} numeros, se encontraron {cont} numeros multiplos de 5')