print('Tarea 15: Problema 8')

terminar = True
while terminar:
    n = input('Inserta un numero entrero del 0 al 9: ')
    if n.isnumeric():
        n = int(n)
        if n >=0 & n <=9:
            if n == 0:
                print('\nCero\n')
            elif n == 1:
                print('\nUno\n')
            elif n == 2:
                print('\nDos\n')
            elif n == 3:
                print('\nTres\n')
            elif n == 4:
                print('\nCuatro\n')
            elif n == 5:
                print('\nCinco\n')
            elif n == 6:
                print('\nSeis\n')
            elif n == 7:
                print('\nSiete\n')
            elif n == 8:
                print('\nOcho\n')
            elif n == 9:
                print('\nNueve\n')
    else:
        if n == 'salir':
            print('\nPrograma terminado\n')
            terminar = False
        