# Map
# map(funcion, objeto iterable)
# devuelve un objeto map
from math import pow
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
numeros = [2,3,4,5,6,7,8,9]
potencias = [2,2,2,2,2,2,2,2]
potenciados = map(pow, numeros, potencias)
print(potenciados)
lista_potenciados = list(potenciados)
print(lista_potenciados)

# programación imperativa

lista1 = [5,8,2,9,3,6]
lista2 = []
for i in lista1:
    lista2.append(i**2)
print(lista2)

# programación funcional (map y reduce)

def cuadrados(num):
    return num**2
lista3 = map(cuadrados, lista1)
print(lista3)

print("----------------------------------------------------------------")
lista4 = tuple(map(cuadrados,lista1))
lista5 = list(map(cuadrados,lista1))
lista6 = set(map(cuadrados,lista1))
print(lista4)
print(lista5)
print(lista6)
print("----------------------------------------------------------------")
# Utilizando lambda para usar map
lista7 = list(map(lambda x: x**2, lista1))
print(lista7)

# Reduce:
# sintaxis reduce(funcion, objeto iterable)
# se debe importar reduce de la libreria functools 

from functools import reduce

lista8 = [1,2,3,4]
# programación imperativa

def funcion_acumulador(acumulador=0, elemento=0):
    return acumulador + elemento

resultado = reduce(funcion_acumulador, lista8)
print(resultado) 

# programación funcional

total = reduce(lambda a,e: a+e, lista8)
print(total)