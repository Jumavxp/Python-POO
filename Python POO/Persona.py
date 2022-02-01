import os
os.system('cls')

class Persona:

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        print('llamando metodo get nombre')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('llamando metodo set nombre')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido (self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'{self._nombre}, {self._apellido}, {self._edad}')

    def __del__(self):
        pass
        
if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 28)
    print(persona1.nombre)











