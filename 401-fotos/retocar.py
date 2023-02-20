# importo la librería de sistema para poder leer directorios
import os
# Importo PIL para poder trabajar con imagenes
from PIL import Image
# Listo los archivos que hay en el directorio actual
archivos = [f for f in os.listdir('.') if os.path.isfile(f)]
# para cada una de las imagenes del directorio
for f in archivos:
    # imprimo la imagen en pantalla
    print(f)
    # Abro la imagen con PIL
    imagen = Image.open(f)
    # Cargo los pixeles que tiene esa imagen
    pixeles = imagen.load()
    # Cargo la altura de la imagen
    altura = imagen.size[1]
    # Cargo detecto la anchura de la imagen
    anchura = imagen.size[0]
    # Para cada uno de los pixles en x
    for x in range(0,anchura):
        # para cada uno de los pixeles en Y
        for y in range(0,altura):
            # Detecto el color rojo de la imagen
            rojo = pixeles[x,y][0]
            # Detecto el color verde de la imagen
            verde = pixeles[x,y][1]
            # Detecto el color azul de la imagen
            azul = pixeles[x,y][2]
            # Como quiero pasarlo a grises obtengo el promedio de los colores
            color = round((rojo+verde+azul)/3)
            # al rojo le asigno el redondeo
            rojo = color
            # al verde le asigno el redondeo
            verde = color
            # al azul le asigno el redondeo
            azul = color
            # actualizo el color del pixel
            pixeles[x,y] = (rojo,verde,azul)
    # por ultimo, guardo la imagen retocada
    imagen.save("./retocadas/"+f)
