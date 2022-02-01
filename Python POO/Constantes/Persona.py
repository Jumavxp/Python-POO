class Persona:
    contador_personas = 0

    @classmethod
    def _generar_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_valor()
        self.nombre = nombre
        self.edad = edad 

    def __str__(self):
        return f'Persona: {self.id_persona}, Nombre: {self.nombre}, edad: {self.edad}'
        

persona1 = Persona ('Juan', 28)
print(persona1)


persona2 = Persona ('Karla', 30)
print(persona2)

print(Persona.contador_personas)