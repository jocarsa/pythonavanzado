#pip install matplotlib
import matplotlib.pyplot as grafica

anchura = 8
altura = 10
figura, eje = grafica.subplots(anchura,altura)

for x in range(0,anchura):
    for y in range(0,altura):
        lista = [523,53,5235,235,2352,34523,5]
        eje[x,y].plot(lista)





grafica.show()
