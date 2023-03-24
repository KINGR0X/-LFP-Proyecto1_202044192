from Abstract.abstract import Expression
from math import *


class Trigonometrica(Expression):

    def __init__(self, left, tipo, fila, columna):
        self.left = left
        self.tipo = tipo

        self.valor = 0
        super().__init__(fila, columna)

    def operar(self, arbol):
        leftValue = ''

        if self.left != None:
            leftValue = self.left.operar(arbol)

        if self.tipo.operar(arbol) == 'Seno':

            grados = leftValue
            radianes = (grados * pi)/180

            resultado = sin(radianes)
            self.valor = resultado

            return resultado

        elif self.tipo.operar(arbol) == 'Coseno':

            grados = leftValue
            radianes = (grados * pi)/180

            resultado = cos(radianes)
            self.valor = resultado

            return resultado

        elif self.tipo.operar(arbol) == 'Tangente':

            grados = leftValue
            radianes = (grados * pi)/180

            resultado = tan(radianes)
            self.valor = resultado

            return resultado

        else:
            return None

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
