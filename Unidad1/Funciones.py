# def saludo():
#     print('Hola mundo')
# saludo()

# def suma(num1, num2): #num1 y num2 son los parametros de la función
#     return num1+num2
# print(suma(15,20))

# def resta(num1, num2): #num1 y num2 son los parametros de la función
#     return num1-num2
# print(resta(10,8))

def operaciones(a,b,operador):
    if operador == '+':
        return a+b
    elif operador == '-':
        return a-b
    elif operador == '*':
        return a*b
    elif operador == '/':
        return a/b
    else:
        return 'Digite un operador válido'

print(operaciones(5,8,'+'))
print(operaciones(5,8,'-'))
print(operaciones(5,8,'*'))
print(operaciones(5,8,'/'))
print(operaciones(5,8,','))