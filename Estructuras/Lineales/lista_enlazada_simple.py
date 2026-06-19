from Estructuras.Lineales.nodo import Node
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

class LinkedList(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Dialog1.ui", self)

        self.head = None
        self.tail = None
        self.agregari.clicked.connect(self.insert_at_beginning)
        self.agregarf.clicked.connect(self.insert_at_end)
        self.imprimir.clicked.connect(self.print_linked_list)
        self.buscar.clicked.connect(self.search)
        self.deletei.clicked.connect(self.delete_at_beginning)
        self.deletef.clicked.connect(self.delete_at_end)

    def insert_at_beginning(self):
        data = self.lineEdit.text()
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self):
        data = self.lineEdit.text()
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_linked_list(self):
        temp = self.head
        texto = "Head -> "

        while temp is not None:
            texto += f"{temp.data} -> "
            temp = temp.next

        texto += "Tail"

        self.lineEdit_2.setText(texto)

    def search(self):
        data = self.lineEdit.text()
        temp = self.head

        while temp is not None:
            if temp.data == data:
                self.lineEdit_2.setText("Elemento encontrado")
                return

            temp = temp.next

        self.lineEdit_2.setText("Elemento no encontrado")

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