import tkinter as tk
# creo la raiz de la ventana
raiz = tk.Tk()
# creo una barra de menu en la memoria
mimenu = tk.Menu(raiz)
# le digo al programa que la barra de menus es la que acabo de crear
raiz.config(menu=mimenu)
# Dentro de la barra de menus, creo la de archivo
menuarchivo = tk.Menu(mimenu)
# Y la añado a la barra de menus
mimenu.add_cascade(label="Archivo",menu=menuarchivo)
# Dentro de la barra de menus, creo la de edicion
menueditar = tk.Menu(mimenu)
# Y la añado a la barra de menus
mimenu.add_cascade(label="Editar",menu=menueditar)
# Dentro de la barra de menus, creo la de ayuda
menuayuda = tk.Menu(mimenu)
# Y la añado a la barra de menus
mimenu.add_cascade(label="Ayuda",menu=menuayuda)
