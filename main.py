#Importem json
import json
#Importem la  classe car de la carpeta Integrant_A
from Integrant_A.Car import Car

#Fem una llista amb 5 instancies
cars = [
    Car("Opel", "Corsa", "2006 KKG", "Gris"),
    Car("Toyota", "Verso", "2007 KKG", "Blanc"),
    Car("Seat", "Ibiza", "2008 KKG", "Vermell"),
    Car("BMW", "A4", "2009 KKG", "Blau"),
    Car("Nissan", "Si", "2001 KKG", "Rosa")
    ]

#Importem la  classe book de la carpeta Integrant_A
from Integrant_A.book import book

#Fem una llista amb 5 instancies
books = [
    book("Lazarillo de tormes", "Castellano", "Alfonso de Valdés", "325", "1554", "novela picaresca"),
    book("Tirat lo Blanc", "Catala", "Joanot Martorell", "325", "1534", "novela"),
    book("Control de oleadas", "Castellano", "Jorge Werlyb", "325", "2019", "novela picaresca"),
    book("Niño con el pijama de rayas", "Castellano", "John Boyne", "325", "2006", "drama total"),
    book("Jacinto y sus flores", "Castellano", "Ramon Font", "2", "2025", "biblia en verso"),
]

#Convertim les llistes a diccionaris
cars_list = [c.to_dict() for c in cars]
books_list = [b.to_dict() for b in books]

#Guardem les llistes en un objecte contenidor
data = {"cars":cars_list, "books":books_list}

#Guardem el objecte contenidor en un arxiu .json
with open("jsonAPI/a.json",'w') as file:
    json.dump(data, file)

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

#Emmagatzemem les llistes a un objecte contenidor en forma diccionari
data = {"gats":gats_list, "escoles":escoles_list}

#Emmagatzemem l'objecte contenidor en un arxiu
with open("jsonAPI/b.json",'w') as file:
    json.dump(data, file)



