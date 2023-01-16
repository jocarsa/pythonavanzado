import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

arbol = ttk.Treeview(raiz)
tablas = arbol.insert("",tk.END,text="Tablas")
vistas = arbol.insert("",tk.END,text="Vistas")

arbol.insert(tablas,tk.END,text="Clientes")
arbol.insert(tablas,tk.END,text="Productos")

arbol.insert(vistas,tk.END,text="Informe 1")
arbol.insert(vistas,tk.END,text="Informe 2")

arbol.pack()

raiz.mainloop()
