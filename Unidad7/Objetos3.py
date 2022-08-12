# Herencia es una relacion entre clases
# Se puede definir una clase de la clase que hereda propiedades y metodo de otra clase
# Clase padre (principal)
# Clase hija (secundaria)
class Persona:
    def crear(self, nombre:str, apellido:str):
        self.nombre = nombre
        self.apellido = apellido
        
    def mostrar(self):
        print(self.nombre, self.apellido)

x = Persona() # Se realizó una instancia de la clase persona
print(type(x))

x.crear('Sergio', 'Romero')
x.mostrar()

class Estudiante:
    
    def __init__(self, name:str, last_name:str):
        self.name = name
        self.last_name = last_name
        self.note = float(input('Digite la nota del estudiante:\n'))
        
    def imprimir(self):
        print(self.name, self.last_name, self.note)
        
    def aprobar(self):
            print('Aprobado') if self.note >= 3.0 else print('No Esta Aprobado')
            
y = Estudiante('Pedro', 'Topo')
y.name = 'Juan'
y.imprimir()
y.aprobar()