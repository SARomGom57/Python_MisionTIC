# *args **kwargs

def suma(*args):
    total = 0
    for i in args:
        total += i
    return total

print(suma(8,9,9,7,6,5))

def suma2(**kwargs):
    total = 0
    for i in kwargs:
        total += kwargs[i]
    return total

print(suma2(a=3, b=14, c=79))