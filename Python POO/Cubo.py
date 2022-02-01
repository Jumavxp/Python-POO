from mimetypes import init
import os 
os.system('cls')

class Cubo:
    def __init__(self, ancho, alto, prof):
        self.ancho = ancho
        self.alto = alto
        self.prof = prof

    def volumen(self):
        return self.ancho*self.alto*self.prof


ancho = int(input('proporcione el ancho: '))
alto = int (input('Proporcione la altura: '))
prof = int (input('Proporcione la profundidad: '))

cubo1 = Cubo(  ancho, alto, prof)
print(f'El volumen es: {cubo1.volumen()}')