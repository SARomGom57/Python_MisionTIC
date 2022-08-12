def cliente(informacion:dict) -> dict:
    if informacion['edad'] > 18:        
        atraccion = 'X-Treme'
        apto = True
        if informacion['primer_ingreso'] == True:
            total_boleta = 20000*0.95 # Calculo de la boleta con descuento
        else:
            total_boleta = 20000  # Valor pleno de la boleta
    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        atraccion = 'Carros chocones'
        apto = True
        if informacion['primer_ingreso'] == True:
            total_boleta = 5000*0.93
        else:
            total_boleta = 5000 
    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        atraccion = 'Sillas voladoras'
        apto = True
        if informacion['primer_ingreso'] == True:
            total_boleta = 10000*0.95
        else:
            total_boleta = 10000 
    else:
        atraccion = 'N/A'
        apto = False
        total_boleta = 'N/A'
        
    informacion_del_parque = {
        'nombre': informacion['nombre'],
        'edad' : informacion['edad'],
        'atraccion' : atraccion,
        'apto' : apto,
        'primer_ingreso' : informacion['primer_ingreso'],
        'total_boleta' : total_boleta 
    }
    
    return informacion_del_parque

informacion1 = {
    'id_cliente': 1,
    'nombre' : 'Johana Fernandez',
    'edad' : 20,
    'primer_ingreso' : True
}

informacion2 = {
    'id_cliente': 1,
    'nombre' : 'Johana Fernandez',
    'edad' : 20,
    'primer_ingreso' : False
}

informacion3 = {
    'id_cliente': 2,
    'nombre' : 'Gloria Suarez',
    'edad' : 3,
    'primer_ingreso' : True
}

print(cliente(informacion1))
print(cliente(informacion2))
print(cliente(informacion3))