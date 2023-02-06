# pip3 install  pandas
# Pandas para tratamiento masivo de información
# pip3 install openpyxl
# Tratamiento concreto de archivos de Excel
import pandas as pan

# creo una lista
n1 = []
# para cada elemento de la lista, desde 1 a 50
for i in range(1,50):
    # inicializo el elemento a cero
    n1.append(0)

registros = pan.read_excel('Euromillones.xlsx')
# recorrer toda la hoja
for fila in registros.values:
    #print(fila[1])
    n1[fila[1]] = n1[fila[1]] + 1
    #for celda in fila:
        #print(celda)
maxn1 = max(n1)
maxin1 = n1.index(maxn1)
print("el valor al que debes jugar es:"+str(maxin1))

# solo quiero un elemento
##valores = registros.values
##print(valores[1][1])
