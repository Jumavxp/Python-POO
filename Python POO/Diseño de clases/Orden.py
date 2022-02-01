from Producto import Producto

class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1 

        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)
    
    def agregar_producto(self,producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total
    
    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + ' \n '
        
        return f'Orden: {self._id_orden}, productos: \n {productos_str} total : {self.calcular_total()} '


if __name__ == '__main__':
    producto1 = Producto('camisa', 100.00)
    producto2 = Producto('pantalon', 150.00 )
    producto3 = Producto('zapatos', 200.00)

    orden1 = Orden([producto1,producto2])
    orden1.agregar_producto(producto3)
    print(orden1)
