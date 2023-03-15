#Importem json per tal de poder treballar amb ell
import json

#Importem les nostres classes i creem cinc instancies de cada una
from Integrant_B.Cat import Cat

gats = [
    Cat("Miauricio","8","8kg","Persa"),
    Cat("Gatamiau","8","10kg","American Shorthair"),
    Cat("Onix","5","7kg","Sphynx"),
    Cat("Lola","2","5kg","Burmés"),
    Cat("Silvestre","10","10kg","Chartreux")
]

from Integrant_B.school import school

escoles = [
    school("Jaime Balmes","Espanya","1942","Batxillerat","Concertat","850"),
    school("Mariano Moreno","Argentina","1898","Primaria","Public","600"),
    school("San Rafael","Ecuador","1915","Primaria","Public","430"),
    school("Rosa dels Vents","Espanya","1949","Secundaria","Public","650"),
    school("Whitney High School","Estats Units","1856","Secundaria","Public","800")
]

#Convertir les instancies a una llista de diccionari JSON
gats_list = [g.to_dict() for g in gats]
escoles_list = [e.to_dict() for e in escoles]

#Emmagatzem les llistes a un objecte contenidor en forma diccionari
data = {"gats":gats_list, "escoles":escoles_list}

#Emmagatzem l'objecte contenidor en un arxiu
with open("jsonAPI2/b.json",'w') as file:
    json.dump(data, file)



