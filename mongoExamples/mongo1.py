from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

# creacion de la conexion
client = MongoClient(MONGO_URI)

# Apunta a la base de datos
db = client['teststore']
# Apunta a la coleccion a manejar
collection = db['products']

# si en el dato no le pasamos un id, mongodb le genera uno 
collection.insert_one({
    "name": "keyboard",
    "price": 300
})

collection.insert_one({
    "_id": 2,
    "name": "mouse",
    "price": 20
})

producte_one = {"name": "Monitor"}
producte_two = {"name": "mousepad"}

collection.insert_many([producte_one,producte_two])

res = collection.find({"name": "keyboard"})
for r in res:
    print(r['name'])