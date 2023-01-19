'''
Las tuplas son estructuras de datos propios de python que permite almacenar distintos valores
y no se pueden reemplazar sus datos
'''

tupla=(1,2,3,"uno","dos")

print(tupla)
tupla2=(7, "Cardiel", True, 12.5, 23+7j)

pritn(tupla[1])
pritn(tupla[4])
pritn(tupla[-1])
pritn(tupla[0:2])
pritn(tupla[2:])

tuplaNueva=tupla+tupla2

print(tuplaNueva)