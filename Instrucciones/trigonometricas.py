import math
from Abstract.abstract import Expression
from math import *


class Trigonometrica(Expression):

    def __init__(self, left, tipo, fila, columna):
        self.left = left
        self.tipo = tipo

        super().__init__(fila, columna)

    def operar(self, arbol):
        leftValue = ''

        if self.left != None:
            leftValue = self.left.operar(arbol)

        if self.tipo.operar(arbol) == 'Seno':
            # se convierte a radianes y se redondea a 2 decimales
            resultado = math.sin(math.radians(leftValue))
            resultado = round(resultado, 2)

            return resultado

        elif self.tipo.operar(arbol) == 'Coseno':

            # se convierte a radianes y se redondea a 2 decimales
            resultado = math.cos(math.radians(leftValue))
            resultado = round(resultado, 2)

            return resultado

        elif self.tipo.operar(arbol) == 'Tangente':

            # se convierte a radianes y se redondea a 2 decimales
            resultado = math.tan(math.radians(leftValue))
            resultado = round(resultado, 2)

            return resultado

        else:
            return None

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
