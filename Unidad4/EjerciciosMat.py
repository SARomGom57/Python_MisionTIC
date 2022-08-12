import numpy as np

matriz = np.zeros((2,3))
print(matriz)
print(type(matriz[1,1]))

matriz2 = np.ones((4,3))
print(matriz2)
print(type(matriz2))

matriz3 = np.full((3,3),'py')
print(matriz3)

matriz4 = np.eye((5)) # matriz identidad
print(matriz4)

import math as m

raiz = m.sqrt(25)
print(raiz)

pi = m.pi
print(pi)

matriz5 = np.random.random((4,4))
print(matriz5)

matriz6 = np.full((4,4), 10)
print(matriz6)

matriz7 = matriz5 * matriz6
print(matriz7)