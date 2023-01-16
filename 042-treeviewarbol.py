import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

arbol = ttk.Treeview(raiz)
arbol.insert("",tk.END,text="Clientes")
arbol.insert("",tk.END,text="Productos")
arbol.pack()

raiz.mainloop()
