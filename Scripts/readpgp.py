import os
import json

def change_ext(file,new_ext):
    nom_bas, ext_act = os.path.splitext(file)
    new_name = nom_bas + new_ext
    os.rename(file,new_name)
    print(f'Archivo renombrado: {new_name}')

def read_file(file):
    with open(file,'r') as archivo:
        content = archivo.read()
    return content

diccionario = json.loads(read_file('./pgps/Algo que decir.pgp'))

print(diccionario['meta']['original'])

# change_ext('./pgps/Algo que decir.pgp','.json')