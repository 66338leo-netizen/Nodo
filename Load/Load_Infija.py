from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from Estructuras.Lineales.Infija_ import InfijaPosfija


class LoadInfija(QDialog):

    def __init__(self):
        super().__init__()

        uic.loadUi("ui/infijas.ui", self)

        self.convertidor = InfijaPosfija()

        self.pushButton.clicked.connect(self.convertir)

    def convertir(self):

        expresion = self.lineEdit.text()

        resultado = self.convertidor.convertir(expresion)

        self.lineEdit_2.setText(resultado)