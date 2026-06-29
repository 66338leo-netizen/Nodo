from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from Load.Load_Infija import LoadInfija
from Load.Load_ import Lista
from Load.Load_1 import LoadStack


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main.ui", self)
        self.actionConvertidor_Infija_Posfija.triggered.connect(self.abrir_infija)
        self.actionLista_Enlazada.triggered.connect(self.abrir_lista)
        self.actionPilas.triggered.connect(self.abrir_pila)
        self.actionSalir.triggered.connect(self.salir)
        self.lista_window = None
        self.stack_window = None
        self.infija_window = None
        
    def abrir_infija(self):
        if self.infija_window is None:
            self.infija_window = LoadInfija()

        self.infija_window.show()
        self.infija_window.raise_()
        self.infija_window.activateWindow()
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