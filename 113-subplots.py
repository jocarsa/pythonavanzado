#pip install matplotlib
import matplotlib.pyplot as grafica

anchura = 4
altura = 4
figura, eje = grafica.subplots(anchura,altura)



valores = ["a","b","c","d","e","f","g"]
lista = [523,53,5235,235,2352,34523,5]
eje[0,1].bar(valores,lista)







grafica.show()
