class Gato:
    
    def __init__ (self, nombre):
        self.nombre=nombre
    def __str__ (self):
        return "Me llamo " + self.nombre
    
g=Gato("Don Gato")
d=Gato("Demóstenes")
print(g)
print(d)

class Chesire(Gato):
    def hablar(self):
        print("Hola Alicia")

c=Chesire("otro")

c.hablar()
    
    
    