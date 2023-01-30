import tkinter as mitk

def dispara():
    print("Lo que has puesto en el campo es:"+contenidoDispara.get())

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
        
