import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()
raiz.title("Aplicación empresarial")
raiz.iconbitmap("favicon.ico")
raiz.geometry("600x600")

def salir():
    exit()

mimenu = tk.Menu(raiz)
raiz.config(menu=mimenu)
menuarchivo = tk.Menu(mimenu)
mimenu.add_cascade(label="Archivo",menu=menuarchivo)
menueditar = tk.Menu(mimenu)
mimenu.add_cascade(label="Editar",menu=menueditar)
menuayuda = tk.Menu(mimenu)
mimenu.add_cascade(label="Ayuda",menu=menuayuda)

# Añado un comando en archivo
menuarchivo.add_command(label="Nuevo")
menuarchivo.add_command(label="Abrir")
menuarchivo.add_command(label="Cerrar")
menuarchivo.add_command(label="Salir",command=salir)
# Añado un comando en edición
menueditar.add_command(label="Copiar")
menueditar.add_command(label="Cortar")
menueditar.add_command(label="Pegar")
menueditar.add_command(label="Deshacer")
# Añado un comando en ayuda
menuayuda.add_command(label="Acerca de")
menuayuda.add_command(label="Versión")

marco1 = tk.Frame(raiz)
marco1.pack()

arbol = ttk.Treeview(marco1)
tablas = arbol.insert("",tk.END,text="Tablas")
vistas = arbol.insert("",tk.END,text="Vistas")
arbol.insert(tablas,tk.END,text="Clientes")
arbol.insert(tablas,tk.END,text="Productos")
arbol.insert(vistas,tk.END,text="Informe 1")
arbol.insert(vistas,tk.END,text="Informe 2")
arbol.grid(row=0,column=0)

tabla = ttk.Treeview(marco1,columns=("identificador", "nombre","apellidos","email","telefono"))
tabla.heading("#0", text="Identificador")
tabla.heading("identificador", text="Id del registro")
tabla.heading("nombre", text="Nombre del cliente")
tabla.heading("apellidos", text="Apellidos del cliente")
tabla.heading("email", text="Correo electrónico")
tabla.heading("telefono", text="Teléfono móvil")
for i in range(0,10):
    tabla.insert(
        "",
        tk.END,
        text="0",
        values=("1", "Jose Vicente","Carratalá Sanchis","info@josevicentecarratala.com","12345")
    )

tabla.grid(row=0,column=1)

raiz.mainloop()






