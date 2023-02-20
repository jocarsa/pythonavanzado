import tkinter as tk


# importo la librería que me permite leer de XML
import xml.etree.ElementTree as ET

# Cargo el xml
arbol = ET.parse('datos.xml')

# me quedo con el elemento principal
raizxml = arbol.getroot()

# creo una nueva ventana de Tkinter
raiz = tk.Tk()
# le doy tamaño
raiz.geometry("800x800")

# creo un nuevo marco dentro de la ventana
marco = tk.Frame()
# empaqueto el marco en la ventana
marco.pack()

def nodo(entrada):
    atributos = entrada.attrib
    imagen = tk.PhotoImage(file = "fotos/1.png")
    labelfoto = tk.Label(image=imagen)
    labelfoto.pack()
    texto = tk.Label(text=atributos['texto'])
    texto.pack()
    pregunta = tk.Label(text=atributos['pregunta'])
    pregunta.pack()
    for hijo in entrada:
        atributoshijo = hijo.attrib
        boton = tk.Button(text=atributoshijo["respuesta"])
        boton.pack()


nodo(raizxml)
