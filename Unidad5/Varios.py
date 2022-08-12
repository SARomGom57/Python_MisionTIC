from functools import reduce
# lista1 = [1,2,3,9,5]
# lista2 = [1,4,5,7,6]
# lista3 = lista1 + lista2
# print(lista3)

lista = [  
    [1201, [4, 25842.99], [18,23254.99], [9, 48951.95]],  
    [1202, [3, 115362.58],[18,2354.99]], 
    [1203, [1, 125698.20], [2, 135645.20], [1, 13645.20],[5, 1645.20]], 
    [1204, [7, 11.99], [11,18.99], [5, 390.95]]
] 

a = 5
 
if a == 5:
    print('Ok')
else:
    print('Error')

print('OK') if a== 5 else print('Error')

# Crear una nueva lista que tenga la siguiente forma:
# [[codigo de la factura, total1, total2, total[n], es cantidad por precio de la unidad]]

lista2 = list(map(lambda x: [x[0]]+list(map(lambda y: y[0]*y[1], x[1:])), lista))
print(lista2)  

# Crear una nueva lista que tenga el total:

lista2 = list(map(lambda x: [x[0]]+[reduce(lambda a,e: a+e, x[1:])], lista2))
print(lista2)

# Crear una lista donde se incluya un bono:

lista2 = list(map(lambda x: x if x[1] < 400000 else [x[0]]+[x[1]-25000],lista2))
print(lista2)