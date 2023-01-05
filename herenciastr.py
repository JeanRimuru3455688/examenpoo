from clase import Juan
from clase import Hello

#REALIZAR UNA HERENCIA ENTRE ARCHIVOS CREANDO UN METODO EN EL HIJO

class Nose(Hello):
    padre = str 
    juan    = Juan("","","")

    def __init__(self, id, nombre, apellido, estatura , padre , juan):
        super().__init__(id, nombre, apellido, estatura)
        self.padre = padre
        self.juan   = juan

    def __str__(self):
        return f"Mi amigo {self.nombre} {self.apellido} mide {self.estatura} y sus padre es {self.padre}"
    
ejemploh = Nose ("3","Maikol", "Chacon", "1.87", "Ricardo", " ")
print(ejemploh)


