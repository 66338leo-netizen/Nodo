from Estructuras.Lineales.nodo import Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_linked_list(self):
        temp = self.head
        result = "Head -> "

        while temp is not None:
            result += f"{temp.data} -> "
            temp = temp.next

        result += "Tail"
        return result

    def search(self, data):
        temp = self.head

        while temp is not None:
            if temp.data == data:
                return "Elemento encontrado"
            temp = temp.next

        return "Elemento no encontrado"

    def delete_at_beginning(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head

            while temp.next != self.tail:
                temp = temp.next

            temp.next = None
            self.tail = temp