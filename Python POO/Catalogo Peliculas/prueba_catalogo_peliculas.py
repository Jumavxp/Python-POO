from dominio.Peliculas import Peliculas
from servicio.CatalogoPeliculas import CatalogoPeliculas

opcion = None

while opcion != 4:
    print('Catalogo Peliculas Menu')
    print('Opciones: ')
    print('1. Agregar Pelicula')
    print('2. Ver lista de peliculas')
    print('3. Eliminar lista')
    print('4. Salir')
    opcion = int(input('Ingrese su opcion (1-4): '))
    if opcion == 1 :
        nombre_pelicula = input('Ingrese el nombre de la pelicula: ')
        pelicula = Peliculas(nombre_pelicula)
        CatalogoPeliculas.agregar_pelicula(pelicula)
    
    elif opcion == 2: 
        CatalogoPeliculas.listar_peliculas()
    
    elif opcion == 3: 
        CatalogoPeliculas.eliminar()      

else:
    print('Salida con exito')