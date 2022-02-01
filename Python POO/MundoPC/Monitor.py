

class Monitor:
    contadorMonitores = 0

    def __init__(self, marca, tamaño):
        self._marca = marca
        self._tamaño = tamaño

        Monitor.contadorMonitores += 1

        self._idMonitor = Monitor.contadorMonitores

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamaño(self):
        return self._tamaño

    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño


    def __str__(self):
        return f'id: {self._idMonitor}, Marca: {self.marca}, Tamaño: {self.tamaño}'


