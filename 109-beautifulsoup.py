# Primero importaremos librerías
# pip install requests
import requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
# pip install lxml 

# Me quiero conectar a una web y sacar su código

with requests.Session() as misesion:
    pagina = misesion.get("https://jocarsa.com")
    #print(pagina.content)

# Quiero poder procesar el código de esa web para sacar los textos
# Para cada una de las direcciones en la lista
for direccion in ['https://jocarsa.com']:
    # en primer lugar intenta
    try:
        respuesta = requests.get(direccion)
        respuesta.raise_for_status()
    # en el caso de que de error http (conexión a internet) sácamelo por pantalla
    except HTTPError as mierror:
        print(mierror)
    # en el caso de que de un error de Python
    except Exception as errorpython:
        print(errorpython)
    # en el caso de que todo vaya bien, sacamos la informacion
    else:
        # le indico el juego de caracteres que se va a encontrar
        respuesta.encoding ='utf-8'
        # proceso el contenido de la web como un arbol xml
        sopa = BeautifulSoup(respuesta.text,'lxml')
        # localizo una etiqueta concreta
        textos = sopa.find_all("p")
        # la imprimo en pantalla
        print(textos)

