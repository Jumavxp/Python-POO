from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclados = 0

    def __init__(self, tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)

        Teclado.contadorTeclados +=1
        self._idTeclado = Teclado.contadorTeclados 

    def __str__(self):
        return f'id: {self._idTeclado}, {super().__str__()}'


#tecladito = Teclado('1', 'tecladito')
#tecladote = Teclado('1', 'tecladote')

#print(tecladito, tecladote)