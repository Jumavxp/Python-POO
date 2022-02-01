
from unicodedata import name


class Producto:
    product_id = 0

    @classmethod
    def id_generator(cls):
        cls.product_id += 1
        return cls.product_id

    def __init__(self, nombre, precio):
        self._id_producto = Producto.id_generator()
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre (self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self,precio):
        self._precio = precio

    @property
    def id_poducto(self):
        return self._id_producto

    def __str__(self):
        return f'Producto: {self._nombre}, ID: {self._id_producto}, precio: {self._precio}'

if __name__ == '__main__': 
    producto1 = Producto('camisa', 100.00)
    producto2 = Producto('pantalon', 150.00 ) 

    print(producto1, producto2)