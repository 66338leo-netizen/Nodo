from Estructuras.Lineales.nodo import Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_beginning(self,data):
        #Paso1: Crear un nuevo nodo
        new_node = Node(data)
        #Paso2: Verificar si la lista esta vacia
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            #Paso3: El nuevo nodo apunta al nodo actual
            new_node.next = self.head
            #Paso4: El nuevo nodo se convierte en la cabeza de la lista
            self.head = new_node
    def print_linked_list(self):
        temp= self.head
        print("Head -> ",end="")
        while temp is not None:
            print(temp.data,"->",end="")
            temp = temp.next
        print(" Tail")
    def insert_at_end(self,data):
        #Paso1: Crear un nuevo nodo
        new_node = Node(data)
        #Paso2: Verificar si la lista esta vacia
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            #Paso3: El nodo actual apunta al nuevo nodo
            self.tail.next = new_node
            #Paso4: El nuevo nodo se convierte en la cola de la lista
            self.tail = new_node
    def search(self,data):
        temp = self.head
        while temp is not None:
            if temp.data == data:                                        
                return True
            temp = temp.next
        return False