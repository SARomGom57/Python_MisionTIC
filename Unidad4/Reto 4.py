def ordenes(rutinaContable):
    from functools import reduce
    totales = list(map(lambda x: [x[0]]+ list(map(lambda y:y[1]*y[2] ,x[1:])),rutinaContable))
    totales = list(map(lambda x: [x[0]] + [reduce(lambda y,z: round(y+z,2),x[1:])],totales))
    totales = list(map(lambda x: x if x[1]>=600000 else [x[0], x[1]+25000 ],totales))   
    print('------------------------ Inicio Registro diario ---------------------------------')
    for i in totales: print(f'La factura {i[0]} tiene un total en pesos de {i[1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------')
    
 
rutinaContable1 = [  
    [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],  
    [1202, ("8756", 3, 115362.58),("1112",18,2354.99)], 
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)], 
    [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]  
]

rutinaContable2 =  [
    [6587, ("3268", 4, 25842.99), ("8274",18,23254.99), ("6548", 9, 48951.95), ("2547", 5, 8951.95)],
    [6588, ("1254", 3, 115362.58), ("9744", 2, 99235.66)]
]

rutinaContable3 =  [
    [6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)], 
    [6590, ("5236", 8, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)], 
    [6591, ("7812", 2, 11.99), ("9652",11,18.99)]
    ]

ordenes(rutinaContable1)
ordenes(rutinaContable2)
ordenes(rutinaContable3)