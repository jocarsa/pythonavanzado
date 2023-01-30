import tkinter as mitk
import random


def dispara():
    print("Lo que has puesto en el campo es:"+contenidoDispara.get())
    print("La letra es: "+contenidoDispara.get()[0])
    print("El número es: "+str(contenidoDispara.get()[1]))
    x = 0
    y = 0
    if contenidoDispara.get()[0] == "A":
        x = 0
    elif contenidoDispara.get()[0] == "B":
        x = 1
    elif contenidoDispara.get()[0] == "C":
        x = 2
    elif contenidoDispara.get()[0] == "D":
        x = 3
    elif contenidoDispara.get()[0] == "E":
        x = 4
    elif contenidoDispara.get()[0] == "F":
        x = 5
    elif contenidoDispara.get()[0] == "G":
        x = 6
    elif contenidoDispara.get()[0] == "H":
        x = 7

    y = int(contenidoDispara.get()[1])-1
    lienzo.create_oval(x*100+30,y*100+30,x*100+70,y*100+70,fill="blue")

        

# la raiz es la ventana
raiz = mitk.Tk()
# esta variable almacena el contenido de Entry
contenidoDispara = mitk.StringVar()

# creo un marco para los parametros
marco = mitk.Frame(raiz)
marco.grid(row=0,column=0)

titulo = mitk.Label(marco,text="Battleship (c)2023 Jose Vicente Carratala")
titulo.pack()

# Guardo el contenido en una variable
entrada = mitk.Entry(marco,textvariable=contenidoDispara)
entrada.pack()

boton = mitk.Button(marco,text="Dispara",command=dispara)
boton.pack()

lienzo = mitk.Canvas(width=800, height=800)
lienzo.grid(row=0,column=1)

for x in range(0,8):
    # x1, y1, x2, y2
    lienzo.create_line(x*100, 0, x*100, 800)
for y in range(0,8):
    lienzo.create_line(0, y*100, 800, y*100)

# voy a crear barcos
for longitud in range(1,6):
    x = random.randint(0,8-longitud)
    y = random.randint(0,8-longitud)
    horizontal = random.randint(0,1)
    lienzo.create_oval(x*100+30,y*100+30,x*100+70,y*100+70+longitud*100,fill="red")


        
