# Funcion lambda
tempo = lambda x: x**2

print(tempo(5))
print(tempo(7))
print(tempo(10))

def operaciones(a,b, fn):
    return fn(a,b)

suma = operaciones(10,9, lambda x, y: x+y)
print(suma)
resta = operaciones(10,9, lambda x, y: x-y)
print(resta)