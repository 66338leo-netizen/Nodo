import sys
from Load.Menu_Principal import Menu
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    ventana = Menu()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()