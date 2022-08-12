# Consigue la @
# data = 'De stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# enlaposicion = data.find('@')
# print(enlaposicion)
# Consigue el espacio luego de uct.ac.za
# espacioenlaposicion = data.find(' ',enlaposicion)
# print(espacioenlaposicion)
# Corta el fragmento localizado previamente
# host = data[enlaposicion+1:espacioenlaposicion]
# print(host)

# def PromedioNotas(dicNotas):
#     sumatoria = 0
#     sumatoria += dicNotas ['nota1']
#     sumatoria += dicNotas ['nota2']
#     sumatoria += dicNotas ['nota3']
#     sumatoria += dicNotas ['nota4']
#     promedioNot = round(sumatoria/4, 2)
#     return promedioNot

# dicNotas = {'nota1' : 3.0, 
#             'nota2' : 2.1, 
#             'nota3' : 5.0,
#             'nota4' : 4.7}

# print('El promedio es:',PromedioNotas(dicNotas))

def reportarPromedio(dicReporte):
    return dicReporte['estudiante']+' = '+str(dicReporte['promedio'])

def generarReporteNotas(dicNotas):
    sumatoria = 0
    sumatoria += dicNotas ['nota1']
    sumatoria += dicNotas ['nota2']
    sumatoria += dicNotas ['nota3']
    sumatoria += dicNotas ['nota4']
    promedio = round(sumatoria/4, 2)
    reporteNotas = {
        'promedio' : promedio,
        'estudiante' : dicNotas['estudiante']
    }
    return reporteNotas
    
dicNotas = {
        'estudiante' : 'Beneficiario Rodriguez',
        'nota1' : 3.0,
        'nota2' : 2.1,
        'nota3' : 5.0,
        'nota4' : 4.7
    }
print(reportarPromedio(generarReporteNotas(dicNotas)))