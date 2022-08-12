# Diseñe una función para calcular la hipotemusa de un triangulo con el teorema de pitagoras
# c = raiz a2 + b2

def hipotemusa(a,b):
    h = (a**2+b**2)**0.5
    return h
print(hipotemusa(5,8))