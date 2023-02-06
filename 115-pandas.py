# pip3 install  pandas
# Pandas para tratamiento masivo de información
# pip3 install openpyxl
# Tratamiento concreto de archivos de Excel
import pandas as pan

registros = pan.read_excel('Euromillones.xlsx')
# recorrer toda la hoja
for fila in registros.values:
    print(fila)
    #for celda in fila:
        #print(celda)

# solo quiero un elemento
valores = registros.values
print(valores[1][1])
