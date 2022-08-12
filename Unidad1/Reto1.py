# def CDT(usuario: str, capital: int, tiempo:int):
#     porcentaje_interes = 0.03
#     porcentaje_perdida = 0.02
#     if tiempo > 2:
#         valor_intereses = (capital*porcentaje_interes*tiempo)/12 #Formula del valor de los intereses
#         valor_total_ganacia = capital+valor_intereses #Formula del valor total
#         return(print(f'Para el usuario {usuario} la cantidad de dinero a recibir, según el monto inicial de ${capital} para un tiempo de {tiempo} meses es: ${valor_total_ganacia}'))
#     else:
#         valor_perder = capital*porcentaje_perdida #Formula del valor a perder
#         valor_total_perdida = capital - valor_perder #Formula del valor total con perdidas
#         return(print(f'Para el usuario {usuario} la cantidad de dinero a recibir, segun el monto inicial de ${capital} para un tiempo de {tiempo} meses es: ${valor_total_perdida}'))

# CDT('AB1012',1000000,3)
# CDT('ER3366',650000,2)
# CDT('QW3456',5000000,2)

def CDT(usuario: str, capital: int, tiempo:int):
    porcentaje_interes = 0.03
    porcentaje_perdida = 0.02
    if tiempo > 2:
        valor_intereses = (capital*porcentaje_interes*tiempo)/12 #Formula del valor de los intereses
        valor_total = capital+valor_intereses #Formula del valor total
    else:
        valor_perder = capital*porcentaje_perdida #Formula del valor a perder
        valor_total = capital - valor_perder #Formula del valor total con perdidas
    return(f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}')

print(CDT('AB1012',1000000,3))
print(CDT('QW3456',5000000,2))