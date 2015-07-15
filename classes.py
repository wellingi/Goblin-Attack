import random

class Players(object):
    def __init__(self):
        self.potions=random.randint(1,2)
        

class Human(Players):
    name=""
    hp=random.randint(8,10)
    attack=random.randint(2,3)
    totalhp=hp
    exp=0
    nextlevel=10
    lvl=1
    totalwins=0
    rest=0

class Goblin(Players):
    hp=random.randint(4,6)
    attack=random.randint(2,4)
    totalhp=hp


ian=Human()
