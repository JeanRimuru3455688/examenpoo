#CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO.
class Juan:
    id        = str
    nombre    = str
    apellido  = str

    def __init__(self, id, nombre, apellido):
        self.id       = id
        self.nombre   = nombre
        self.apellido = apellido

    def Valo(self):
        print("su nombre es " + self.nombre + " y su apellido es  " + self.apellido )

test1 = Juan("1" ,"Anthony", "franco")
test2 = Juan("2", "Jareth", "Mejia")

test1.Valo()
test2.Valo()


#REALIZAR UNA HERENCIA DENTRO DEL MISMO ARCHIVO DE UNA DE LAS CLASES CREADAS, CREANDO UN METODO STR EN EL HIJO (IMPRMIR UN OBJETO CON ESA CLASE)
class Hello(Juan):
    estatura = str 
    
    def __init__(self, id, nombre, apellido, estatura):
        super().__init__(id, nombre, apellido)
        self.estatura = estatura
        
    def __str__(self):
        return f"Mi mejor amigo {self.nombre} {self.apellido} mide {self.estatura}"

ejemplo = Hello("1", "Pedro", "Zavala" , "1.67")
print(ejemplo)