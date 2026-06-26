from Estructuras.Lineales.pilas_stacks import Stack
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog


class LoadStack(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/pilas_qdialog.ui", self)

        self.pila = Stack()

        self.pushButton.clicked.connect(self.eliminar)
        self.pushButton_2.clicked.connect(self.mostrar_tope)
        self.pushButton_3.clicked.connect(self.imprimir_pila)
        self.pushButton_4.clicked.connect(self.agregar)

    def agregar(self):
        texto = self.lineEdit.text().strip()

        if texto == "":
            return

        self.pila.push(texto)
        self.lineEdit.clear()

    def eliminar(self):
        self.pila.pop()

    def mostrar_tope(self):
        self.lineEdit_2.setText(self.pila.top_of_stack())

    def imprimir_pila(self):
        self.lineEdit_2.setText(self.pila.print_stack())