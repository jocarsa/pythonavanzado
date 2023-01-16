import tkinter as tk

raiz = tk.Tk()

etiqueta = tk.Label(raiz,text="Hola")
etiqueta.pack()
etiqueta.config(fg="red",bg="white")
etiqueta.config(font="Arial 44")
print(etiqueta.config())

raiz.mainloop()
