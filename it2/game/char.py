from weapons import Weapons
from random import randint 

class Character: 
    def __init__(self, carName:str, weapon:int, strength:int, hp:int):
        self._carName = carName
        self._weapon = weapon
        self._strength = strength
        self._hp = hp
    
    def __str__(self):
        return f"Your name is {self._carName}, your weapon is {self._weapon}, you have {self._strength} strength and {self._hp} hp"
    
    def attack(self):
        critRate = randint(1, 2)
        dmgBuff = self._strength * 2
        atk = self._weapon =+ dmgBuff
        critDmg = atk * critRate
        return critDmg
    
    def dmgTaken(self, damage):
        self._hp =- damage
        if self._hp > 0:
            print(f"you have {self._hp} remaining")
        if self._hp < 0:
            self._hp = 0 
            
     