num_inicial = int(input('Inserte el numero inicial: '))
num_final = int(input('Inserte el numero final: '))

positivos = 0
negativos = 0

for i in range(num_inicial, num_final + 1):
    if i > 0:
        positivos += 1
    elif i < 0:
        negativos += 1

print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)


dias = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']
 
for dia in dias:
    if dia == "Lunes":
        continue
    elif dia == 'Viernes':
        break
    print(dia)