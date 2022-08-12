from email.headerregistry import ContentTransferEncodingHeader


a = True
b = False
print(type(a), type(b))
print(a)
print(not(a))
print(5>8)
print(8>5)

# Sensor puerta --> true: puerta abierta y false: puerta cerrada 
# Sensor ventana --> false: ventana abierta y true: ventana cerrada 
# Hacer un programa que encienda una alarma cuando o la ventana o la puerta o ambas esten abiertas

ventana = True
puerta = False
if puerta or not(ventana):
    print('alarma encendida')
else:
    print('alarma apagada')