#Se crea la classe "gat" con la cual trabajaremos conceptos OOP
class Cat:
    #Definimos un constructor el cual tiene como parametroes 4 atributos
    def __init__(self, nombre, peso, raza, edad):
        self.nombre = nombre
        self.peso = peso
        self.raza = raza
        self.edad = edad

#Trabajamos el metodo getter y setter de cada atributo que hemos especificado anteriormente en el constructor.
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    def getRaza(self):
        return self.raza

    def setRaza(self, raza):
        self.raza = raza

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    #Metodo que nos permitira ver los atributos de nuestro objeto.
    def salutacio(self):
        print(f"El nom del gat és: {self.nombre}"
            f"\n L'edat del gat és: {self.edad}"
            f"\n El pes del gat és: {self.peso}"
            f"\n La raça del gat és: {self.raza}")
    
    #Metodo que nos permitira retornar el objeto en formato json
    def to_dict(self):
        return{
            "nom":self.nombre,
            "edat":self.edad,
            "pes":self.peso,
            "raça":self.raza
        }
