import pandas as pd

inventario = {
    'Impresora': ['Hp', 'Epson', 'Canon'],
    'Cantidad': [8,10,5]
}

InvPandas = pd.DataFrame(inventario)
print(inventario)
print('----------------------------------------------------------------')
print(InvPandas)
print(type(InvPandas))
# Los dataframes van de la mano con los diccionarios

ciudades = ['Cali', 'Barranquilla', 'Cartagena']
SerPandas = pd.Series(ciudades)
print(ciudades)
print(SerPandas)

ventas = {
    'enero': 2000000,
    'febrero': 3500000,
    'marzo': 4000000
}

ventasPen = pd.Series(data = ventas, axis = ['enero', 'febrero', 'marzo'])
print(ventasPen)