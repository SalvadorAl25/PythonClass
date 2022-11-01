r1 = int(input('Inserta el inicio del rango: '))

r2 = int(input('Inserta el final del rango: '))

ri = r1

con = 0

while r1 < r2:
    r1 += 1
    con += 1
print(f'entre {ri} y {r2}, hay {con} numeros')