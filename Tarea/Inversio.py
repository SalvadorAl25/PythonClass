print('Tarea 3: Problema 3')

nr =''
terminar = True
while terminar:
    ##ingresa el dato
    num = input('ingresa un numero de 5 digitos: ')
    ##valida si es un digito
    if num.isdigit():
        ##valida si es un digito de 5 numeros
        if len(num) == 5:
            ##convierte el tipo de dato a entero
            num = int(num)
            print('------------------------------')
            ##invierte el digito
            for i in range(5):
                r = int(num % 10)
                nr = nr+str(r)
                num = num / 10
                print(nr)
            terminar = False
            print('------------------------------')
            print('¡Numero invertido!\n')
        else:
            print(f'{num} no tiene 5 digitos...')
    else:
        print(f'{num} no es un numero...')