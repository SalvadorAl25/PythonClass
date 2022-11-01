num = input('Inserta un numero: ')

i=0
if num.isdigit():
    while i < len(num):
        i += 1
    print(f'El numero tiene {i} digitos')