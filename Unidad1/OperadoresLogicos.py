# Realizar un programa que indique si una persona debe presentar
# la declaración de renta. Las condiciones para presentar estos impuestos son:
# Ser mayor de edad 
# Tener ingresos superiores o iguales a $50.831.000

edad =int(input('Digite su edad: '))
ingresos = int(input('¿Cuáles son sus ingresos mensuales? '))
ingreso_anual = ingresos * 12
# if edad > 17 and ingreso_anual >= 50831000:
#     print('Usted debe presentar declaración de renta')
# else:
#     print('Usted no debe presentar declaración de renta')

if edad < 18 or ingreso_anual < 50831000:
    print('Usted no debe presentar declaración de renta')
else:
    print('Usted debe presentar declaración de renta')