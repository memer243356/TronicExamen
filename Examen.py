#sistema de gestion  de biblioteca, debe de tener por lo menos dos clases, 
#libro y  Biblioteca; libro debe de tener, titulo autorm año de publicacion, y disponibilidad del libro
#ademas la clase libro debe de tener los siguientes metodos, prestar, devolver e informacion
#biblioteca debe de tener la clase de libros y los metodos ; agregar libro, mostrar inventario y buscar libro

variables = {}

class biblioteca:
    class libro:
        def __init__(self, autor, ADP, DdelL):
            self.autor = autor
            self.ADP = ADP
            self.DdelL = DdelL
        
        def exposicion(self):
            print("Nombre del libro actual es: ", self.autor)
            print("Año de Publicacion del Libro es: ",self.ADP)
            print("Disponibilidad del Libro", self.DdelL)


    def agregar_libro(self):
        nombre = input("Ingrese el nombre del libro: ")
        valor = input(f"Ingrese el año de publicacion de {nombre}: ")        
        variables[nombre] = valor
        print(f"Variable '{nombre}' agregada con valor '{valor}'\n")
        
    
    def mostrar_inventario(self):
        print("Variables disponibles:")
        for nombre, valor in variables.items():
            print("el libro" , {nombre}, "con fecha de creacion", {valor}," y esta disponible")      

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while True:                  
    print("Bienvenido a la Gestion de la Biblioteca Tronic")
    print("Que Deseas hace?")
    print("agregar libro = 1")
    print("mostar libros = 2")
    print("")
    print("salir = 0")
    eleccion=int(input(">"))

    if eleccion == 1:
        agregar = biblioteca()
        agregar.agregar_libro()
    elif eleccion ==2:
        mostrar = biblioteca()
        mostrar.mostrar_inventario()
    elif eleccion == 0:
        print("Gracias")
        break
    else:
        print("no hay esa opcion")