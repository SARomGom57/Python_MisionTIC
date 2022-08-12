# POO Programacion Orientada a Objetos
# Python es un lenguaje orientado a objectos
# Casi todo en Phyton es un objecto
# Clase: Es un modelo o patron del cual se puede crear multiples objetos
# Hay que crear la clase, se definen las propiedades o atributos y metodos y funciones
# Cuando se crea un objeto, es lo mismo que decir crear una INSTNACIA de la clase

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

# Metodo constructor, es un metodo que se ejecuta automatique cuando el objeto es creado
# En Python, ese metodo se llama __init__
# Es un metodo especial, su principal objetivo es inicializar los atributos o propiedades de un objeto
# Este metodo no retorna datos y recibe parametros para inicializar los atributos

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
