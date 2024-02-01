#realiza_un_programa_para_gestionar_una_libreria.

class libreria:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"libro '(libro)' añadido correctamente")
    
    def mostrar_libro(self):
        if not self.libros:
            print("la libreria esta vacia.")
        else:
            print("lista de libros:")
            for i, libro in enumerate(self.libros, 1):
                print(f"{i}. {libro}")
    
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"libro '{libro}' eliminado correctamente.")
        else:
            print(f"libro '{libro}'no encontrado en la libreria")

#solicitar_la_libreria
mi_libreria = libreria()

while True:
    print("\n---Menu de la libreia ---")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Eliminar libro")
    print("4. salir")

    opcion = input("Selecciona una opcion (1-4): ")

    if opcion == "1":
        nuevo_libro = input("Ingresa el nombre del nuevo libro: ")
        mi_libreria.agregar_libro(nuevo_libro)
    elif opcion == "2":
        mi_libreria.mostrar_libros()
    elif opcion == "3":
        libro_a_eliminar = input("Ingresar el nombre del libro a eliminar: ")
        mi_libreria.eliminar_libro(libro_a_eliminar)
    elif opcion == "4":
        print("Saliendo del programa. ¡Ingrese el nombre del libro a eliminar: ")
        break
    else:
        print("Opcion no valida. por favor, selecciona una opcion valida (1-4). ")
