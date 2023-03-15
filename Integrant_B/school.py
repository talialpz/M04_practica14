#Se crea la clase school que nos permitira trabajar con los conceptos de la programación orientada a objetos.
class school:

    #Definimos un constructor el cual tiene como parametro 6 atributos.
    def __init__(self, nombre, pais, año, etapa, financiacion, capacidad):
        self.nombre = nombre
        self.pais = pais
        self.año = año
        self.etapa = etapa
        self.financiacion = financiacion
        self.capacidad = capacidad

    #Trabajamos el metodo getter y setter de cada atributo que hemos especificado anteriormente en el constructor.
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getPais(self):
        return self.pais

    def setPais(self, pais):
        self.pais = pais

    def getAño(self):
        return self.año

    def setAño(self, año):
        self.año = año

    def getEtapa(self):
        return self.etapa

    def setEtapa(self, etapa):
        self.etapa = etapa

    def getFinanciacion(self):
        return self.financiacion

    def setFinanciacion(self, financiacion):
        self.financiacion = financiacion

    def getCapacidad(self):
        return self.capacidad

    def setCapacidad(self, capacidad):
        self.capacidad = capacidad

    #Creamos un mensaje que permita ver los atributos de nuestro objeto.
    def info(self):
        txt = "El colegio {nom} se encuentra en {pa} y fue inaugurado en {año}. Su etapa llega hasta {et}, con una capacidad de {cap} personas y es de caracter {fin}"
        print(txt.format(nom = self.nombre, pa = self.pais, año = self.año, et = self.etapa, cap = self.capacidad, fin = self.financiacion))

    #Metodo que nos permitira retornar el objeto en formato json
    def to_dict(self):
        return{
            "nom":self.nombre,
            "pais":self.pais,
            "any":self.año,
            "etapa":self.etapa,
            "financiacio":self.financiacion,
            "capacitat":self.capacidad
        }