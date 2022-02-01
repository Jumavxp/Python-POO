from FiguraGeometrica import *
from Color import *


class Rectangulo (FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color) 

    def Area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f' Ancho: {self._ancho} Alto: {self._ancho} Color: {self._color}'
        

rectangle1 = Rectangulo(15,15, 'Aka')

print(f'{rectangle1}')