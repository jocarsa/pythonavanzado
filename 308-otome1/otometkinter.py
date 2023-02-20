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
marco = tk.Frame(raiz)
# empaqueto el marco en la ventana
marco.pack()

# defino un nodo genérico y reutilizable
# defino una función reutilizable
def nodo(entrada):
    # cargo los atributos de esa entrada
    #atributos = entrada.attrib
    ######################################### IMAGEN
    # cargo una imagen desde el disco
    imagen = tk.PhotoImage(file = "fotos/1.png")
    # la imagen tiene que existir en un label
    labelfoto = tk.Label(marco,image=imagen)
    # muestro el label
    labelfoto.pack()
    etiqueta = tk.Label(text="hola")
    etiqueta.pack()
    ######################################### TEXTO
    # de momento saco el texto
    #print(atributos['texto'])

    # de momento saco la pregunta
    #print(atributos['pregunta'])
    # ahora quiero las preguntas
##    for pregunta in entrada:
##        # para cada pregunta cargos sus atributos
##        atributospregunta = pregunta.attrib
##        # imprimo los atributos por pantalla
##        print(atributospregunta['opcion']+": "+atributospregunta['respuesta'])
    #eleccion = input("Escoge una opción ")
    #print("Has escogido la opción "+eleccion)
    #for hijo in entrada:
        #atributos = hijo.attrib
        #if atributos['opcion'] == eleccion:
            #nodo(hijo)



# uso la función
nodo(raizxml)
