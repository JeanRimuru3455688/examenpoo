from clase import Juan
from clase import Hello
from herenciastr import Nose
from clasestr import Mamigo

#REALIZAR UNA HERENCIA EN UNA CLASE QUE CONTENGA VARIOS OBJETOS (2) Y OBJETOS DENTRO DE OBJETOS (2)

class Objetos(Mamigo):
    nacio    = str
    juan     = Juan("","","")
    hello    = Hello("","","","")
    nose     = Nose("","","","",Hello("","","",""))
    mamigo   = Mamigo("","","","")
    
    def __init__(self, nombre, apellido, telefono, edad , juan , hello , nose , mamigo):
        super().__init__(nombre, apellido, telefono, edad)
        self.juan    = juan
        self.hello   = hello 
        self.nose    = nose 
        self.mamigo  = mamigo

    def Vobjetos(self):
        print("El " + self.nombre + self.apellido + " si tengo su numero es " + self.telefono + "y su edad es " + self.edad)

ejemplo1 = Objetos("Francisco", "Narval" , "08478197764", "21" , Juan("2", "Dany", "Jose"), Hello("56", "Sebas", "navas", "1.89"), Nose("45", "jean", "vera", "1,80", "Pedro"), Mamigo("David", "vega", "04775867897", "25"))

ejemplo1.Vobjetos()
print(vars(ejemplo1))
print(vars(ejemplo1.juan))
print(vars(ejemplo1.juan.hello))
print(vars(ejemplo1.nose))
print(vars(ejemplo1.hello))
print(vars(ejemplo1.mamigo))