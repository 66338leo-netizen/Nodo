from Estructuras.Lineales.lista_enlazada_simple import LinkedList

class menu():
    def __init__(self):
        self.linked_list = LinkedList()
    def menu_principal(self):
        while True:
            print("1. Insertar al inicio")
            print("2. Insertar al final")
            print("3. Imprimir")
            print("4. Buscar")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                data = input("Ingrese el dato a insertar al inicio: ")
                self.linked_list.insert_at_beginning(data)
            elif opcion == "2":
                data = input("Ingrese el dato a insertar al final: ")
                self.linked_list.insert_at_end(data)
            elif opcion == "3":
                self.linked_list.print_linked_list()
            elif opcion == "4":
                data = input("Ingrese el dato a buscar: ")
                found = self.linked_list.search(data)
                if found:
                    print(f"El elemento '{data}' se encuentra en la lista.")
                else:
                    print(f"El elemento '{data}' no se encuentra en la lista.")
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")