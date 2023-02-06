#pip install matplotlib
import matplotlib.pyplot as grafica


figura, eje = grafica.subplots(3,3)

for x in range(0,3):
    for y in range(0,3):
        lista = [523,53,5235,235,2352,34523,5]
        eje[x,y].plot(lista)





grafica.show()
