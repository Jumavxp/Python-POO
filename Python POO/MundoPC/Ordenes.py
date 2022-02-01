

class Ordenes:
    contador = 0
    def __init__(self, computadoras):
        Ordenes.contador+=1
        self.idOrden = Ordenes.contador
        self._computadoras = list(computadoras)

    def agregar_compu(self, computadora):
        self._computadoras.append(computadora)


    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

        return f'''
        Orden: {self.idOrden}
        Computadoras: {computadoras_str}
        '''