import tkinter as tk
from functools import partial


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



def iterar(elemento,respuesta):
    #print("vamos a iterar")
    #nodo(elemento)
    print("el elemento es:")
    print(elemento)
    print("Y la respuesta es:")
    print(respuesta)
    for hijo in elemento:
        atributos = hijo.attrib
        if atributos['respuesta'] == respuesta:
            labelfoto.destroy()
            texto.destroy()
            pregunta.destroy()
            for boton in botones:
                boton.destroy()
            nodo(hijo)

def nodo(entrada):
    global labelfoto
    global texto
    global pregunta
    global botones
    global imagen
    atributos = entrada.attrib
    imagen = tk.PhotoImage(file = "fotos/"+atributos["imagen"])
    labelfoto = tk.Label(image=imagen)
    labelfoto.pack()
    texto = tk.Label(text=atributos['texto'])
    texto.pack()
    pregunta = tk.Label(text=atributos['pregunta'])
    pregunta.pack()
    botones = []
    for hijo in entrada:
        botones.append("")
    contador = 0
   
    for hijo in entrada:
        atributoshijo = hijo.attrib
        print("la respuesta que voy  a enviar es:"+atributoshijo["respuesta"])
        botones[contador] = tk.Button(text=atributoshijo["respuesta"],command=partial(iterar, entrada,atributoshijo["respuesta"]))
        botones[contador].pack()
        contador = contador + 1
    


nodo(raizxml)

