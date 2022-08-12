#Realice un programa que detecte si un numero es par o no
numero = int(input('Digite el numero:\n'))
#módulo de dos numeros arroja el residuo de la división
#ejemplo 9 módulo 3 es 0
#ejemplo 8 módulo 3 es 2
#El operador del módulo en python es el %

if numero%2 == 0:
    print('El numero es par')
else:
    print('El numero es impar')

#Operadores:
#Aritmeticos: + - * / % ** //
#Relacionales: < <= > >= == =!
#Logicos: and or not