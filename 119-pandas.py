# pip3 install  pandas
# Pandas para tratamiento masivo de información
# pip3 install openpyxl
# Tratamiento concreto de archivos de Excel
import pandas as pan

# creo una lista
n1 = []
n2 = []
n3 = []
n4 = []
n5 = []
e1 = []
e2 = []
# para cada elemento de la lista, desde 1 a 50
for i in range(1,52):
    # inicializo el elemento a cero
    n1.append(0)
    n2.append(0)
    n3.append(0)
    n4.append(0)
    n5.append(0)
    e1.append(0)
    e2.append(0)


registros = pan.read_excel('Euromillones.xlsx')
# recorrer toda la hoja
for fila in registros.values:
    n1[fila[1]] = n1[fila[1]] + 1
    n2[fila[2]] = n2[fila[2]] + 1
    n3[fila[3]] = n3[fila[3]] + 1
    n4[fila[4]] = n4[fila[4]] + 1
    n5[fila[5]] = n5[fila[5]] + 1
    e1[fila[6]] = e1[fila[6]] + 1
    e2[fila[7]] = e2[fila[7]] + 1


maxin1 = n1.index(max(n1))
maxin2 = n2.index(max(n2))
maxin3 = n3.index(max(n3))
maxin4 = n4.index(max(n4))
maxin5 = n5.index(max(n5))
maxin6 = e1.index(max(e1))
maxin7 = e2.index(max(e2))
print("el valor al que debes jugar es: "+str(maxin1))
print("el valor al que debes jugar es: "+str(maxin2))
print("el valor al que debes jugar es: "+str(maxin3))
print("el valor al que debes jugar es: "+str(maxin4))
print("el valor al que debes jugar es: "+str(maxin5))
print("estrella 1: "+str(maxin6))
print("estrella 2: "+str(maxin7))

# solo quiero un elemento
##valores = registros.values
##print(valores[1][1])
