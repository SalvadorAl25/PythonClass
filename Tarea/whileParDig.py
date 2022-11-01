n = input('Inserte un numero: ')

n = list(n)
par = 0
i=0
while i<len(n):
    if int(n[i]) % 2 == 0:
        par += 1
    i += 1
print(f'en el numero se encontraron {par} numeros par') 