import tkinter as tk
# creo una nueva ventana de Tkinter
raiz = tk.Tk()
# le doy tamaño
raiz.geometry("800x800")

# creo un nuevo marco dentro de la ventana
marco = tk.Frame()
# empaqueto el marco en la ventana
marco.pack()

# cargo una imagen desde el disco
imagen = tk.PhotoImage(file = "fotos/1.png")
# la imagen tiene que existir en un label
labelfoto = tk.Label(marco,image=imagen)
# muestro el label
labelfoto.pack()

# creo otro label
texto = tk.Label(marco,text="Este es el texto de inicio")
texto.pack()
