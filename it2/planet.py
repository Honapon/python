import math as m

class planet:
    
    def __init__(self, navn, radius, solavstand, index):
        self._navn = navn
        self._radius = radius
        self._solavstand = solavstand
        self._index = index
    
    def printNavn(self):
        print(self._navn)
    
    def endreNavn(self, nyttNavn):
        self._navn = nyttNavn
        
    def volum(self):
        volum = 4/3*m.pi*self._radius**3
        return volum
        
mars = planet("Mars", 3389.5, 22*10**9, 4)


mars.printNavn()
print(mars.volum())
