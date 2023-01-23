import tkinter as tk
from random import randint
import math
# condiciones iniciales
anchura = 1600
altura = 1600


class Persona:
    def __init__(self):
        self.edad = randint(0,100)
        self.posicionx = randint(0,anchura)
        self.posiciony = randint(0,altura)
        self.angulo = randint(0,360)
    def mover(self):
        self.posicionx = self.posicionx + math.cos(math.radians(self.angulo))
        self.posiciony = self.posiciony + math.sin(math.radians(self.angulo))
    def colisionaParedes(self):
        if self.posicionx < 0 or self.posicionx > anchura or self.posiciony < 0 or self.posiciony > altura:
            self.angulo = self.angulo + 180
            

# establezco un limite en 18
numeropersonas = 180
# creo una lista vacía de jugadores
jugadores = []
# en un bucle for repito un numero X de veces
for i in range(0,numeropersonas):
    # añado un nuevo jugador a esa lista
    jugadores.append(Persona())


class Aplicacion(object):
    def __init__(self,master):
        # función de inicio
        print("yo soy el constructor")
        # cojo el master que viene en el parámetro y lo pongo como propiedad del objeto
        self.master = master
        # dentro de X milisegundos, entro en el bucle
        self.master.after(1000,self.bucle)
    def bucle(self):
        # borro todo lo que había antes
        lienzo.delete("all")
        # función de bucle
        print("estas en el bucle")
        # Meto los jugadores en el bucle
        for i in range(0,numeropersonas):
            #print("Jugador "+str(i)+": posx "+str(jugadores[i].posicionx)+" / posy "+str(jugadores[i].posiciony))
            jugadores[i].mover()
            jugadores[i].colisionaParedes()
            lienzo.create_oval(
                jugadores[i].posicionx,
                jugadores[i].posiciony,
                jugadores[i].posicionx+10,
                jugadores[i].posiciony+10,
                fill="red")
        # dentro de X milisegundos, entro en el bucle
        self.master.after(100,self.bucle)

raiz = tk.Tk()

marco = tk.Frame(width=anchura,height=altura) 
lienzo = tk.Canvas()
lienzo.pack()


aplicacion = Aplicacion(raiz)






