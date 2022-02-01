from email import message
import os
os.system("cls")

class Rectangulo:

    def __init__(self):
        self.base = int(input('Ingrese la base del reactangulo: '))

        self.altura = int(input('Ingrese la altura del rectangulo: '))
        

    def Area(self):    
        return f'El area del reactangulo es: {self.base*self.altura}'


rectangulo1 = Rectangulo()
rectangulo2 = Rectangulo()

print(rectangulo2.Area())
print(rectangulo1.Area())