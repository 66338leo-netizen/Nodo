from Estructuras.Lineales.pilas_stacks import Stack


class InfijaPosfija:

    def __init__(self):
        self.pila = Stack()

    def prioridad(self, operador):
        if operador == "$":
            return 3
        elif operador == "*" or operador == "/":
            return 2
        elif operador == "+" or operador == "-":
            return 1
        return 0

    def convertir(self, expresion):

        expresion = expresion.replace(" ", "")
        resultado = ""

        while not self.pila.is_empty():
            self.pila.pop()

        for caracter in expresion:

            if caracter.isalnum():
                resultado += caracter

            elif caracter == "(":
                self.pila.push(caracter)

            elif caracter == ")":

                while (not self.pila.is_empty()) and self.pila.top_of_stack() != "(":
                    resultado += self.pila.top_of_stack()
                    self.pila.pop()

                if not self.pila.is_empty():
                    self.pila.pop()

            else:

                while (not self.pila.is_empty()) and \
                      self.pila.top_of_stack() != "(" and \
                      self.prioridad(self.pila.top_of_stack()) >= self.prioridad(caracter):

                    resultado += self.pila.top_of_stack()
                    self.pila.pop()

                self.pila.push(caracter)

        while not self.pila.is_empty():
            resultado += self.pila.top_of_stack()
            self.pila.pop()

        return resultado