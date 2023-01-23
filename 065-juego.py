import tkinter as tk
# condiciones iniciales


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
        # dentro de X milisegundos, entro en el bucle
        self.master.after(1000,self.bucle)

raiz = tk.Tk()
aplicacion = Aplicacion(raiz)

