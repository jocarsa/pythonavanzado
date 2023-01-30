import tkinter as mitk

#la raiz es la ventana
raiz = mitk.Tk()

# creo un marco para los parametros
marco = mitk.Frame(raiz)
marco.grid(row=0,column=0)

titulo = mitk.Label(marco,text="Battleship (c)2023 Jose Vicente Carratala")
titulo.pack()

entrada = mitk.Entry(marco)
entrada.pack()

boton = mitk.Button(marco,text="Dispara")
boton.pack()

lienzo = mitk.Canvas(width=800, height=800)
lienzo.grid(row=0,column=1)

for x in range(0,8):
    lienzo.create_line(x*100, 0, x*100, 800)
for y in range(0,8):
    lienzo.create_line(0, y*100, 800, y*100)
        
