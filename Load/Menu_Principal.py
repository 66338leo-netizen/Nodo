from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from Load.Load_1 import LoadStack
from Load.Load_  import Lista

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main.ui", self)

        self.actionLista_Enlazada.triggered.connect(self.abrir_lista)
        self.actionPilas.triggered.connect(self.abrir_pila)
        self.actionSalir.triggered.connect(self.salir)

        self.lista_window = None
        self.stack_window = None

    def abrir_lista(self):
        if self.lista_window is None:
            self.lista_window = Lista()

        self.lista_window.show()
        self.lista_window.raise_()
        self.lista_window.activateWindow()

    def abrir_pila(self):
        if self.stack_window is None:
            self.stack_window = LoadStack()

        self.stack_window.show()
        self.stack_window.raise_()
        self.stack_window.activateWindow()

    def salir(self):
        self.close()