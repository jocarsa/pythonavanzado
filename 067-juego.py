import tkinter as tk
from random import randint
# condiciones iniciales

class Persona:
    def __init__(self):
        self.edad = 0
        self.posicionx = randint(0,200)
        self.posiciony = randint(0,200)

# establezco un limite en 18
numeropersonas = 18
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
        # función de bucle
        print("estas en el bucle")
        # Meto los jugadores en el bucle
        for i in range(0,numeropersonas):
            print("Jugador "+str(i)+": posx "+str(jugadores[i].posicionx)+" / posy "+str(jugadores[i].posiciony))
            lienzo.create_oval(
                jugadores[i].posicionx,
                jugadores[i].posiciony,
                jugadores[i].posicionx+10,
                jugadores[i].posiciony+10,
                fill="red")
        # dentro de X milisegundos, entro en el bucle
        self.master.after(1000,self.bucle)

raiz = tk.Tk()

marco = tk.Frame(raiz,width=400,height=400) 
lienzo = tk.Canvas()
lienzo.pack()


aplicacion = Aplicacion(raiz)






