#CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO __str__

class Mamigo:
    nombre   = str
    apellido = str
    telefono = str
    edad     = str

    def __init__(self, nombre, apellido, telefono, edad):

        self.nombre   = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.edad     = edad 

    def __str__(self):
        return f"Mi mejor amigo {self.nombre} {self.apellido} tiene la edad de {self.edad} y su telefono es {self.telefono}"

ejemplo = Mamigo("Pedro", "Simba" , "09968678712" , "19")
print(ejemplo)