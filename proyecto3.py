class Autor:
    def __init__(self, nombre,apellidos):
        self.Nombre = nombre
        self.Apellidos = apellidos
    def MostrarAutor(self):
        print("Autor: ",self.Nombre," ",self.Apellidos)

class Libro:
    def __init__(self, titulo, isbn):
        self.Titulo = titulo
        self.ISBN = isbn
    def AnadirAutor(self, autor):
        self.Autor = autor
    def MostrarLibro(self):
        print("-----Libro------")
        print("Titulo: ",self.Titulo)
        print("ISBN: ",self.ISBN)
        print("----------------")
    def ObtenerTitulo(self):
        return self.Titulo

class Biblioteca:
    def __init__(self):
        self.ListaLibros = []
    def NumeroLibros(self):
        return len(self.ListaLibros)
    def AñadirLibro(self,libro):
        self.ListaLibros = self.ListaLibros + [libro]
    def MostrarBiblioteca(self):
        print("#############################")
        for item in self.ListaLibros:
            item.MostrarLibro()
        print("#############################")
    def BorrarLibro(self, titulo):
        encontrado = False
        posicionaborrar = -1
        for item in self.ListaLibros:
            posicionaborrar += 1
            if item.ObtenerTitulo() == titulo:
                encontrado = True
                break
            if encontrado:
                del self.ListaLibros[posicionaborrar]
                print("Libro borrado correctamente!")
            else:
                print("Libro no encontrado")
    
def MostrarMenu():
    print("\nMenu\n1) Añadir libro a la biblioteca\n2) Mostrar biblioteca\n3) Borrar libro\n4) ¿Numero de libros?\n5) Salir\n")
    
def AñadirLibroBiblioteca(biblioteca):
    titulo = input("Insertar titulo del libro: ")
    isbn = input("Inserta el ISBN del libro: ")
    autornombre = input("Inserta el nombre del autor: ")
    autorapellido = input("Insertar el apellido del autor: ")
    autor = Autor(autornombre,autorapellido)
    libro = Libro(titulo,isbn)
    libro.AnadirAutor(autor)
    biblioteca.AñadirLibro(libro)
    return biblioteca
def MostrarBiblioteca(biblioteca):
    biblioteca.MostrarBiblioteca()

def BorrarLibro(biblioteca):
    titulo = input("Inserta el titulo del libro a borrar: ")
    biblioteca.BorrarLibro(titulo)
    
def NumeroLibros(biblioteca):
    print("El numero de libros en la biblioteca es: ",biblioteca.NumeroLibros())
    
    
fin = False
biblioteca = Biblioteca()

while not fin:
    MostrarMenu()
    opcion = int(input("Selecciona una opcion: "))
    if(opcion == 1):
        biblioteca = AñadirLibroBiblioteca(biblioteca)
    elif(opcion == 2):
        MostrarBiblioteca(biblioteca)
    elif(opcion == 3):
        BorrarLibro(biblioteca)
    elif(opcion == 4):
        NumeroLibros(biblioteca)
    elif(opcion == 5):
        fin = True
print("Programa terminado")