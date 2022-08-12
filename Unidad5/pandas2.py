import pandas as pd
import numpy as np
# Crear un data frame a partir de un array numpy
arreglo = np.array([[4,5,2],[4,5,8],[1,4,3]])
print(arreglo)
df0 = pd.DataFrame(arreglo)
print(df0)