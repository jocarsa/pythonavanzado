# importo la librería que me permite leer de XML
import xml.etree.ElementTree as ET
# Cargo el xml
arbol = ET.parse('datos.xml')
# me quedo con el elemento principal
raiz = arbol.getroot()
# de momento trabajo solo con la raiz
print(raiz)
atributos = raiz.attrib
print(atributos['texto'])
print(atributos['pregunta'])
# ahora voy a ver cuantos elementos hijos tiene la raiz

for i in raiz:
    atributos = i.attrib
    print(atributos['opcion']+": "+atributos['respuesta'])
    
eleccion = input("Escoge una opción ")
print("Has escogido la opción "+eleccion)

for i in raiz:
    atributos = i.attrib
    if atributos['opcion'] == eleccion:
        print(atributos['texto'])

