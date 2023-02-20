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
    # creo una lista de grises
    grises = []
    for i in range(0,256):
        grises.append(0)
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
            grises[color] = grises[color] + 1
    # por ultimo, guardo la imagen retocada
    #imagen.save("./retocadas/"+f)
    print(grises)
    minimo = 0
    for i in range(0,len(grises)):
        if grises[i] > 50:
            minimo = i
            break

    print("el minimo es:"+str(minimo))

    maximo = 0
    for i in range(len(grises)-1,0,-1):
        if grises[i] > 50:
            maximo = i
            break
    print("el maximo es:"+str(maximo))
    # ahora que ya tengo la imagen con rangos, voy a corregir
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
            rojo = round(rojo*(255/maximo))
            verde = round(verde*(255/maximo))
            azul = round(azul*(255/maximo))
            pixeles[x,y] = (rojo,verde,azul)
    imagen.save("./retocadas/"+f)
            
             













        
