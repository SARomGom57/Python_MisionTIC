# Clase llamada operaciones donde se cargan 2 numeros
# Metodo __init__ y 4 metodos para las operaciones aritmeticas basicas

class Operaciones:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    def sum(self):
        print(f'La suma es: {self.x+self.y:.2f}')
    def sub(self):
        print(f'La resta es: {self.x-self.y:.2f}')
    def mul(self):
        print(f'La multiplicación es: {self.x*self.y:.2f}')
    def div(self):
        print(f'La división es: {self.x/self.y:.2f}')
        
z = Operaciones(25.51, 16.64)
z.sum()
z.sub()
z.mul()
z.div()