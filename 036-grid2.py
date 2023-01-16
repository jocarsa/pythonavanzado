import tkinter as tk

raiz = tk.Tk()

etiqueta = tk.Label(raiz,text="Arriba izquierda")
etiqueta.grid(row=0,column=0)
etiqueta2 = tk.Label(raiz,text="Arriba derecha")
etiqueta2.grid(row=0,column=1)

etiqueta3 = tk.Label(raiz,text="Abajo izquierda")
etiqueta3.grid(row=1,column=0)
etiqueta4 = tk.Label(raiz,text="Abajo derecha")
etiqueta4.grid(row=1,column=1)

etiqueta5 = tk.Label(raiz,text="Necesito que este texto me ocupe dos columnas")
etiqueta5.grid(row=2,column=0,columnspan=2)

raiz.mainloop()
