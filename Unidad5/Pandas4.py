import pandas as pd
df1 = pd.read_csv('titanic3.csv')
print(df1.columns)
print(df1['ticket'])
print(df1.ticket)
df2 = df1.sex
print(type(df1), type(df2))
df3 = df1[['ticket','sex','age']]
print(type(df3))
print(df3)
print(df1[10:21])
print(df1.iloc[20])
print(df1[df1.age==20])
print(df1[df1.age>=21])