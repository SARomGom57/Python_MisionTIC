# Operaciones entre conjuntos
CarbohidratosNat = {'Papa', 'Yuca', 'Ñame'}
CarbohidratosPro = {'Harina de Trigo', 'Pasta','Pan'}
# Operadores de conjuntos
# | unión
# & intersección
# - Diferencia
# ^ Diferencia simetrica
print(len(CarbohidratosPro))
print(len(CarbohidratosNat))
print(CarbohidratosPro|CarbohidratosNat)
print(CarbohidratosPro&CarbohidratosNat)
print(CarbohidratosPro-CarbohidratosNat)
print(CarbohidratosPro^CarbohidratosNat)

Lista = [2,2,2,3,6,5,4,8,7,5,8,6,1,4,5,3,2,6,9,1,4,5,6,2,3,5]
Conjunto = set(Lista)
print(Conjunto)