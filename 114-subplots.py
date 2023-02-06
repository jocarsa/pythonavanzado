#pip install matplotlib
import matplotlib.pyplot as grafica
import csv

anchura = 4
altura = 4
figura, eje = grafica.subplots(anchura,altura)
file = open("precios.txt", "r")
data = list(csv.reader(file, delimiter=","))
print(data[0])


lista = data[0]
numeros = [eval(i) for i in lista]
eje[0,1].plot(numeros)







grafica.show()
