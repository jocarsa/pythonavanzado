import tkinter as tk

raiz = tk.Tk()

def oculta():
    etiqueta.forget()
    etiqueta2.pack()
    etiqueta3.pack()

etiqueta = tk.Label(raiz,text="Esta es la primera pantalla")
etiqueta.pack()

etiqueta2 = tk.Label(raiz,text="Esta es la segunda pantalla")
etiqueta3 = tk.Label(raiz,text="Esto también va en la segunda pantalla")

boton1 = tk.Button(raiz,text="Pulsame",command=oculta)
boton1.pack()
