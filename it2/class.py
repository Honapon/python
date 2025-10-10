# class personer:
#     def __init__(self, fir, las, yrBo):
#         self._fir = fir
#         self._las = las
#         self._born = yrBo
#     def printPers(self):
#         print(self._fir, self._las)

# John = personer("John", "Doe", 1969)
# personer.printPers(John)

# class car:
#     def __init__(self, owner, make, model, year):
#         self._owner = owner
#         self._make = make
#         self._model = model
#         self._year = year
#     def printOwner(self):
#         print("Eier er:", self._owner)
#     def printCar(self):
#         print(f"Du eier en: {self._make} {self._model}, {self._year} modell.")
# fred = car("Fredrik","Toyota", "yaris", 1999)
# karl = car("Karl", "Ford", "Maverick", 2025)

# car.printCar(fred)

# class student:
#     def __init__(self, name, score, quizzes):
#         self._name = name
#         self._score = score
#         self._quizzes = quizzes
#     def leggTilQuizScore(self, score):
#         self._score += score
#         self._quizzes += 1
#         print(f"Du:{self._name}, score: {self._score}, antall quiz: {self._quizzes}")

# tor = student("Tor", 0, 0)

# tor.leggTilQuizScore(88)
# tor.leggTilQuizScore(4)    
from adresse import Adresse
class Person:
    def __init__(self, navn:str, alder:int, adresse:Adresse):
        self._navn = navn
        self._alder = alder
        self._adresse = adresse
    
    def visGatenavn(self):
        self._adresse.visGate()
    
adresse1 = Adresse("kabelgata 24", "Oslo")
person1 = Person("Abc", 24, adresse1)
person1.visGatenavn()