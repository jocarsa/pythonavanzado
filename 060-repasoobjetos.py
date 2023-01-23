class Persona:
    def __init__(self,minombre):
        self.edad = 0
        self.nombre = minombre
    def correr(self):
        print(self.nombre+" está corriendo")

jugadores = []
jugadores.append(Persona("Juan"))
jugadores.append(Persona("Pedro"))
jugadores.append(Persona("Daniel"))

print(jugadores[0].edad)
jugadores[0].correr()
