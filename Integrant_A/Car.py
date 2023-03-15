#Creem la classe
class Car:
    def __init__(self, marca, matricula, model, color):
        self.marca = marca
        self.matricula = matricula
        self.model = model
        self.color = color
        
    
    #Definim els getters i setters
    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca

    def getMatricula(self):
        return self.matricula
    
    def setMatricula(self, matricula):
        self.matricula = matricula

    def getModel(self):
        return self.model
    
    def setModel(self, model):
        self.model = model
    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

    #Aquesta funció ens printejarà agafarà el valor de la class en la frase
    def salutacio(self):
        print("La marca és " + self.marca + ", el seu model és " + self.model + " la matricula és " + self.matricula + " el color és " + self.color)
    
    def to_dict(self):
        return {
            "marca":self.marca,
            "matricula":self.matricula,
            "model":self.model,
            "color":self.color
        }