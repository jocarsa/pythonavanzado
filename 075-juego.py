import tkinter as tk
from random import randint
import math
# condiciones iniciales
anchura = 600
altura = 600
fps = 30


class Persona:
    def __init__(self):
        self.edad = randint(0,100)
        self.posicionx = randint(0,anchura)
        self.posiciony = randint(0,altura)
        self.angulo = randint(0,360)
        self.rojo = randint(0,255)
        self.verde = randint(0,255)
        self.azul = randint(0,255)
    def mover(self):
        self.posicionx = self.posicionx + math.cos(math.radians(self.angulo))
        self.posiciony = self.posiciony + math.sin(math.radians(self.angulo))
    def colisionaParedes(self):
        if self.posicionx < 0 or self.posicionx > anchura or self.posiciony < 0 or self.posiciony > altura:
            self.angulo = self.angulo + 180
            

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
        self.lienzo = tk.Canvas(self.master,width=anchura,height=altura)
        self.lienzo.pack()
        # dentro de X milisegundos, entro en el bucle
        self.master.after(1000,self.bucle)
    def bucle(self):
        # borro todo lo que había antes
        self.lienzo.delete("all")
        # función de bucle
        #print("estas en el bucle")
        # Meto los jugadores en el bucle
        for i in range(0,numeropersonas):
            #print("Jugador "+str(i)+": posx "+str(jugadores[i].posicionx)+" / posy "+str(jugadores[i].posiciony))
            jugadores[i].mover()
            jugadores[i].colisionaParedes()
            comporojo = str(hex(jugadores[i].rojo)[2:]).zfill(2)
            compoverde = str(hex(jugadores[i].verde)[2:]).zfill(2)
            compoazul = str(hex(jugadores[i].azul)[2:]).zfill(2)
            self.lienzo.create_oval(
                jugadores[i].posicionx,
                jugadores[i].posiciony,
                jugadores[i].posicionx+10,
                jugadores[i].posiciony+10,
                fill="#"+comporojo+compoverde+compoazul+"")
            # voy a calcular la colision
            for j in range(0,numeropersonas):
                # no te calcules la colisión de ti contigo mismo
                if i != j:
                    a = jugadores[i].posicionx - jugadores[j].posicionx;
                    b = jugadores[i].posiciony - jugadores[j].posiciony;
                    c = math.sqrt( a*a + b*b );
                    if c < 5:
                        print("colision")
        # dentro de X milisegundos, entro en el bucle
        self.master.after(round(1000/fps),self.bucle)

raiz = tk.Tk()

#marco = tk.Frame(width=anchura,height=altura) 
#lienzo = tk.Canvas()
#lienzo.pack()


aplicacion = Aplicacion(raiz)






