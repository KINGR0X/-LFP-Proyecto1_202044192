from Abstract.abstract import Expression


class Aritmetica (Expression):

    def __init__(self, left, right, tipo, fila, columna):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        leftValue = ''
        rightValue = ''

        if self.left != None:
            leftValue = self.left.operar(arbol)

        if self.right != None:
            rightValue = self.right.operar(arbol)

        if self.tipo.operar(arbol) == 'Suma':

            resultado = leftValue+rightValue

            return resultado

        elif self.tipo.operar(arbol) == 'Resta':

            resultado = leftValue - rightValue

            return resultado

        elif self.tipo.operar(arbol) == 'Multiplicacion':

            resultado = leftValue * rightValue

            return resultado

        elif self.tipo.operar(arbol) == 'Division':

            resultado = leftValue / rightValue

            return resultado

        elif self.tipo.operar(arbol) == 'Modulo':

            resultado = leftValue % rightValue

            return resultado

        elif self.tipo.operar(arbol) == 'Potencia':

            resultado = leftValue ** rightValue

            return resultado

        elif self.tipo.operar(arbol) == 'Raiz':

            resultado = leftValue ** (1/rightValue)

            return resultado

        elif self.tipo.operar(arbol) == 'Inverso':

            resultado = 1/leftValue

            return resultado

        else:
            return None

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
