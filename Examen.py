#sistema de gestion  de biblioteca, debe de tener por lo menos dos clases, 
#libro y  Biblioteca; libro debe de tener, titulo, autor, año de publicacion, y disponibilidad del libro
#ademas la clase libro debe de tener los siguientes metodos, prestar, devolver e informacion
#biblioteca debe de tener la clase de libros y los metodos ; agregar libro, mostrar inventario y buscar libro

variables = {}

class biblioteca:

    def agregar_libro(self):
        nombre = input("Ingrese el nombre del libro: ")
        fecha = (input(f"Ingrese el año de publicacion de {nombre}: "))
        autor = input(f"Ingrese el autor de {nombre}: ")  
        self.variables[nombre] = {"fecha" : fecha, "autor" : autor}
        print("")
        
    
    def mostrar_inventario(self):
        print("Libros disponibles:")
        for nombre, atributos in variables.items():
            fecha = atributos["fecha"]
            autor = atributos["autor"]
            print(f"el libro {nombre} siendo creado por {autor} con fecha de creacion {fecha} y esta disponible\n")      

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while True:                  
    print("Bienvenido a la Gestion de la Biblioteca Tronic")
    print("Que Deseas hace?")
    print("agregar libro = 1")
    print("mostar libros = 2")
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