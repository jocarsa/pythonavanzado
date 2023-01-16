import tkinter as tk

raiz = tk.Tk()

etiqueta = tk.Label(raiz,text="Hola mundo")
etiqueta.grid(row=0,column=0)
etiqueta2 = tk.Label(raiz,text="Hola mundo2")
etiqueta2.grid(row=0,column=1)

raiz.mainloop()
