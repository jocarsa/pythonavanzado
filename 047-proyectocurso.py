import tkinter as tk

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


raiz.mainloop()
