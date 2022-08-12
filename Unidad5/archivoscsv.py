import pandas as pd

diccionario = {
    'first_name': ['Sigrid', 'Joe', 'Theodoric', 'Kennedy', 'Beatrix', 'Olimpia', 'Grange','Sallee'],
    'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Pärlett', 'Guenther', 'Douce', 'Johnstone'],
    'age': [27,31,36,53,48,36,40,34],
    'amount1': [7.17,1.90,1.11,1.41,6.69,4.62,1.01,4.88],
    'amount2': [8.06,'?',5.90,'?','?',7.48,4.37,'?']
}

# df1 = pd.DataFrame(diccionario)
# print(df1)
# df1.to_csv('EjemploCsv.csv', sep='|', header=None)
# df2 = pd.read_csv('EjemploCsv.csv')
# print(df2)
# df3 = pd.read_csv('EjemploCsv.csv', sep='|')
# print(df3)

df1 = pd.read_csv('D:\\Dropbox\\Mision TIC 2022\\Grupo 19\\Ciclo 1\\Fundamentos de Programación\\Unidad 5\\Casos_positivos_de_COVID-19_en_ColombiaDiezMil(1).csv')
print(df1)