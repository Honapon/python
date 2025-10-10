from char import Character
from weapons import Weapons
from random import randint

gameRunning = False
def playerChar():
    global player, enemy, gameRunning
    weapon1 = Weapons("hero", "polearm", 20)
    weapon2 = Weapons("ushigatana", "sword", 10)
    name = input("Whats your name?: ")
    weapon = input(f"choose your weapon: {weapon1.choice()}, {weapon2.choice()}: ")
    
    if weapon == "1":
        cold = weapon1._dmg
        hot = randint(10, 25)
    elif weapon == "2":
        cold = weapon2._dmg
        hot = randint(5,15)
    else:
        cold = 1
        print("slurs")
        exit()
        
    player = Character(name, cold, 10, 400)

    enemy = Character("minority", hot, 7, 400)
    gameRunning = True

playerChar()

def printStart():
    print("|__________________|")
    print("|------Ni hao------|")
    
def choise():
    print("|------ choose an action ------|")
    print("|      Press 1 for Attack      |")
    print("|     Press 2 for HP stats     |") 
    print("|      Press 3 to give up      |")      
    return input("What do you choose?: ")

printStart()
#
while gameRunning:
    choice = choise()
    
    if choice == "1":
        a=1
    elif choice == "2":
        print("poo")
    else: 
        gameRunning = False
        print("game end u suck")
        