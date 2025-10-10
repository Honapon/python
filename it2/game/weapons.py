class Weapons:
    def __init__(self, name:str, wpType:str, dmg:int):
        self._name = name
        self._wpType = wpType
        self._dmg = dmg
    def __str__(self):
        return f"Your weapon is a {self._wpType} named {self._name}."
    def damage(self):
        return self._dmg
    def choice(self):
        return f"weapon: {self._name}"

weapon1 = Weapons("hero", "polearm", 20)
weapon2 = Weapons("ushigatana", "sword", 10)

# print(weapon, weapon.damage())
         