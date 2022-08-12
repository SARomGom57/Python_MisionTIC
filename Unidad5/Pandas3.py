import pandas as pd

df1 = pd.read_csv('titanic3.csv')

print(df1.head(15)) # print 15 primeras lineas
print(df1.tail(15)) # print 15 ultimas lineas
print(df1.shape)
print(df1.columns)
print(pd.unique(df1['pclass'])) # Imprime una lista de los datos unicos de la columna
print(df1['age'].value_counts()) # cuenta los datos unicos de la columna
print(df1['age'].describe()) # muestra un resumen de datos de estadistica descriptiva
print(df1['age'].min())
print(df1['age'].max())
print(df1['age'].mean())

datosGrupoEdad = df1.groupby('age')
print(datosGrupoEdad.describe())
print(datosGrupoEdad.max())
