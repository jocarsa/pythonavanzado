import tkinter as tk

raiz = tk.Tk()

def pantalla2():
    marco1.forget()
    marco2.pack()

marco1 = tk.Frame(raiz)
marco1.pack()

etiqueta1 = tk.Label(marco1,text="Si estas viendo esto, es la primera pantalla")
etiqueta1.pack()
etiqueta2 = tk.Label(marco1,text="Esto también pertenece a la primera pantalla")
etiqueta2.pack()

marco2 = tk.Frame(raiz)


etiqueta3 = tk.Label(marco2,text="Si estas viendo esto, es la segunda pantalla")
etiqueta3.pack()
etiqueta4 = tk.Label(marco2,text="Esto también pertenece a la segunda pantalla")
etiqueta4.pack()

boton = tk.Button(raiz,text="Vamos a la segunda pantalla",command=pantalla2)
boton.pack()
