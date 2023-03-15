#Creem la classe
class book:
    def __init__(self, name, language, author, pages, year, gender):
        self.name = name
        self.language = language
        self.author = author
        self.pages = pages
        self.year = year
        self.gender = gender
    
    #Definim els getters i setters
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getLanguage(self):
        return self.language
    
    def setLanguage(self, language):
        self.language = language

    def getAuthor(self):
        return self.author
    
    def setAuthor(self, author):
        self.author = author
    
    def getPages(self):
        return self.pages
    
    def setPages(self, pages):
        self.pages = pages

    def getYear(self):
        return self.year
    
    def setYear(self, year):
        self.year = year

    def getGender(self):
        return self.gender
    
    def setGender(self, gender):
        self.gender = gender

    #Aquesta funció ens printejarà agafarà el valor de la class en la frase
    def info(self):
        print("El titol és " + self.name + ", el seu genere és " + self.gender + " està escrit per " + self.author + " que el va escriure en el " + self.year + " en " + self.language + " i té " + self.pages + " pàgines")

    def to_dict(self):
        return {
            "name":self.name,
            "language":self.language,
            "author":self.author,
            "pages":self.pages,
            "year":self.year,
            "gender":self.gender
        }    