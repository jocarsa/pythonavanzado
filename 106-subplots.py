#pip install matplotlib
import matplotlib.pyplot as grafica


figura, eje = grafica.subplots(3,3)


lista = [523,53,5235,235,2352,34523,5]
eje[0,0].plot(lista)
grafica.ylabel("mi colección de numeros")
grafica.show()
