# importo la librería que me permite leer de XML
import xml.etree.ElementTree as ET
# Cargo el xml
arbol = ET.parse('datos.xml')
# me quedo con el elemento principal
raiz = arbol.getroot()
#quiero sacarlo por pantalla
print(raiz)
for i in raiz:
    atributos = i.attrib
    print("etiqueta: "+i.tag)
    print("identificador:"+atributos['id'])
    print("contenido de la pregunta:"+atributos['pregunta'])
