import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

tabla = ttk.Treeview(columns=("identificador", "nombre","apellidos","email","telefono"))
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

tabla.pack()

raiz.mainloop()
