import os
os.system('cls')


from Empleado import Empleado
from Gerente import Gerente



def imprimir_detalles(objeto):
    #print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.depart)


empleado1 = Empleado('Juan', 5000)
imprimir_detalles(empleado1)

gerente1 = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente1)