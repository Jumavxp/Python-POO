from FiguraGeometrica import * 
from Color import *

class Cuadrado (FiguraGeometrica, Color):
    def __init__(self,  lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def Area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f' Ancho: {self._ancho} Alto: {self._ancho} Color: {self._color}'

cuadrado1 = Cuadrado(15, 'azul')

print(cuadrado1.__str__())