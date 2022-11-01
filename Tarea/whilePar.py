ri = int(input('Inserte inicio del rango: '))

rf = int(input('Inserte final del rango: '))

par = 0

while ri < rf:
    if ri % 2 == 0:
        par += 1
    ri += 1
print(f'dentro del rango se encuentran {par} numeros pares')