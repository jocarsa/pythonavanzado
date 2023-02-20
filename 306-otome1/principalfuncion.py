# importo la librería que me permite leer de XML
import xml.etree.ElementTree as ET

# Cargo el xml
arbol = ET.parse('datos.xml')

# me quedo con el elemento principal
raiz = arbol.getroot()

# defino un nodo genérico y reutilizable
# defino una función reutilizable
def nodo(entrada):
    # cargo los atributos de esa entrada
    atributos = entrada.attrib
    # de momento saco el texto
    print(atributos['texto'])
    # de momento saco la pregunta
    print(atributos['pregunta'])
    # ahora quiero las preguntas
    for pregunta in entrada:
        # para cada pregunta cargos sus atributos
        atributospregunta = pregunta.attrib
        # imprimo los atributos por pantalla
        print(atributospregunta['opcion']+": "+atributospregunta['respuesta'])
    eleccion = input("Escoge una opción ")
    print("Has escogido la opción "+eleccion)
    for hijo in entrada:
        atributos = hijo.attrib
        if atributos['opcion'] == eleccion:
            nodo(hijo)

# uso la función
nodo(raiz)


