import tkinter as tk
from tkinter import ttk
import mysql.connector

raiz = tk.Tk()
raiz.title("Aplicación empresarial")
raiz.iconbitmap("favicon.ico")
raiz.geometry("600x600")

# Me conecto al servidor y guardo la conexión
conexion = mysql.connector.connect(
    host = "localhost",
    user = "curso",
    password = "curso",
    port = 3306,
    database = "curso"
    )
# Creo un cursor para ejecutar peticiones
micursor = conexion.cursor()

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
# Ejecuto una consulta
micursor.execute("SHOW TABLES")
miresultado = micursor.fetchall()
for resultado in miresultado:
    print(resultado[0])
    arbol.insert(tablas,tk.END,text=resultado[0])

arbol.insert(vistas,tk.END,text="Informe 1")
arbol.insert(vistas,tk.END,text="Informe 2")
arbol.grid(row=0,column=0)

def clickArbol(event):
    # tengo x e y
    print(event)
    # identifica qué elemento está en esa x y en esa y
    item = arbol.identify('item',event.x,event.y)
    # imprime no ya esta entidad, sino el texto de la entidad
    # voy a trabajar con una nueva tabla
    print("voy a trabajar con la tabla: ", arbol.item(item,"text"))
    # para ello, me cargo la tabla anterior de la memoria
    #tabla.delete()
    # tambien la elimino de la interfaz
    tabla.grid_forget()
    # quiero saber las columnas que tiene esta tabla
    micursor.execute("SHOW COLUMNS FROM "+str(arbol.item(item,"text")))
    miresultado = micursor.fetchall()
    columnas = []
    for resultado in miresultado:
          columnas.append(resultado[0])
    # quiero ver el listado de columnas
    print(columnas)
    # creo una nueva tabla con las nuevas columnas
    nuevatabla = ttk.Treeview(marco1,columns=columnas)
    # lo maqueto en la interfaz
    nuevatabla.grid(row=0,column=1)
    # creo la cabecera de la primera columna (id de python)
    nuevatabla.heading("#0", text="Id del arbol")
    # para cada una de las columnas de la base de datos
    for columna in columnas:
        # añado columna en el arbol en formato tabla
        nuevatabla.heading(columna, text=columna)
    

arbol.bind("<Button>", clickArbol)

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






