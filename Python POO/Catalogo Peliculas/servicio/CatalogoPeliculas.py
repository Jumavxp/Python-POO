import os

class CatalogoPeliculas:
    ruta_archivo ='pelicula.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8')as archivo:
            archivo.write(f'-{pelicula.nombre}\n')
        print('Pelicula agregada')
            
    @classmethod
    def listar_peliculas(cls):
        try:
            with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
                print(archivo.read())
        except Exception as e:
            print('Ocurrio un error', e)
    
    @classmethod
    def eliminar(cls):
        os.remove(cls.ruta_archivo)
        print('Archivo eliminado correctamente')