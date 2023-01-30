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

lienzo = mitk.Canvas()
lienzo.grid(row=0,column=1)
