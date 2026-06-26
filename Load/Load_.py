from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from Estructuras.Lineales.lista_enlazada_simple import LinkedList


class Lista(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Dialog1.ui", self)
        self.lista = LinkedList()

        self.agregari.clicked.connect(self.insert_beginning)
        self.agregarf.clicked.connect(self.insert_end)
        self.imprimir.clicked.connect(self.print_list)
        self.buscar.clicked.connect(self.search_value)
        self.deletei.clicked.connect(self.delete_beginning)
        self.deletef.clicked.connect(self.delete_end)

    def insert_beginning(self):
        data = self.lineEdit.text()
        self.lista.insert_at_beginning(data)
        self.lineEdit.clear()

    def insert_end(self):
        data = self.lineEdit.text()
        self.lista.insert_at_end(data)
        self.lineEdit.clear()

    def print_list(self):
        self.lineEdit_2.setText(self.lista.print_linked_list())

    def search_value(self):
        data = self.lineEdit.text()
        self.lineEdit_2.setText(self.lista.search(data))

    def delete_beginning(self):
        self.lista.delete_at_beginning()
        self.lineEdit_2.setText(self.lista.print_linked_list())

    def delete_end(self):
        self.lista.delete_at_end()
        self.lineEdit_2.setText(self.lista.print_linked_list())