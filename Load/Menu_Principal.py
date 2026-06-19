from Estructuras.Lineales.lista_enlazada_simple import LinkedList
import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main.ui", self)
        self.actionLista_Enlazada.triggered.connect(self.menu_principal)
        self.actionSalir.triggered.connect(self.Salir)
        
    def menu_principal(self):
        self.linked_list = LinkedList()
        self.linked_list.show()
    def Salir(self):
        self.close()
           