# pip3 install  pandas
# Pandas para tratamiento masivo de información
# pip3 install openpyxl
# Tratamiento concreto de archivos de Excel
import pandas as pan
import matplotlib.pyplot as plt

#fig = plt.figure()

#ax = fig.add_axes([0,0,1,1])

# creo una lista
numero = []
estrella = []
etiquetanumero = []

# para cada elemento de la lista, desde 1 a 50
for i in range(1,52):
    # inicializo el elemento a cero
    numero.append(0)
    estrella.append(0)
    etiquetanumero.append(str(i-1))


registros = pan.read_excel('Euromillones.xlsx')
# recorrer toda la hoja
for fila in registros.values:
    numero[fila[1]] = numero[fila[1]] + 1
    numero[fila[2]] = numero[fila[2]] + 1
    numero[fila[3]] = numero[fila[3]] + 1
    numero[fila[4]] = numero[fila[4]] + 1
    numero[fila[5]] = numero[fila[5]] + 1
    estrella[fila[6]] = estrella[fila[6]] + 1
    estrella[fila[7]] = estrella[fila[7]] + 1


print(numero)
print(estrella)

for i in range(1,51):
    print("El numero: "+str(i)+" ha salido "+str(numero[i]))


plt.bar(etiquetanumero,numero,label=etiquetanumero)
plt.show()





