from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado

class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):

        Computadora.contador_computadora += 1 
        self._idComp = Computadora.contador_computadora

        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}:{self._idComp}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''


if __name__ == '__main__':
    monitor1 = Monitor('HP', '15 Pulg')
    raton1 = Raton('USB', 'HP')
    teclado1 = Teclado('USB', 'HP')
    compu1 = Computadora('HP', monitor1, teclado1, raton1)
    
    print(compu1)