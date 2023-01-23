class Persona:
    def __init__(self,minombre):
        self.edad = 0
        self.nombre = minombre
    def correr(self):
        return self.nombre+" está corriendo"

jugadores = []
jugadores.append(Persona("Juan"))
print("La edad de Juan es:"+str(jugadores[0].edad))

jugadores[0].edad = jugadores[0].edad + 5

print("La edad de Juan es:"+str(jugadores[0].edad))
