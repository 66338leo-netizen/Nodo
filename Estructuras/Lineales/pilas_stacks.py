from Estructuras.Lineales.nodo import Node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        nuevo_nodo = Node(data)
        nuevo_nodo.next = self.top
        self.top = nuevo_nodo

    def pop(self):
        if self.top is None:
            return

        self.top = self.top.next

    def top_of_stack(self):
        if self.top is None:
            return ""

        return str(self.top.data)

    def print_stack(self):
        if self.top is None:
            return ""

        aux = self.top
        contenido = ""

        while aux is not None:
            contenido += str(aux.data)

            if aux.next is not None:
                contenido += "\n---\n"

            aux = aux.next

        return contenido