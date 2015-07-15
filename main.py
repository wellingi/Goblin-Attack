from random import randint
from classes import *
import os

#clear screen
def erase():
    os.system('clear')

player=Human()


names=[   #Names for Monsters
"Clyde",
"Oscar",
"Perrywinkle",
"Fitzy",
"Fredrick"
]

def rest():#rest timer
    erase()
    if player.rest >=5:
         player.hp=player.totalhp
    else:
        print "Sorry you are not tired enough to rest"
    menu()
     

def levelup(): # Level UP
    player.lvl+=1
    player.exp=0
    player.nextlevel=10*(player.lvl+2)
    player.hp+=(.5*player.hp)
    player.attack+=1
    print "You Gained a Level!"


def attack(attacker, defender):   #Def attack fuction
    attack=attacker.attack
    defender.hp-=attacker.attack
    print "It hit for %d damage" % attack
    
        
def heal (attacker):   #Def heal fuction
    erase()
    if attacker.potions >0:
        attacker.hp=attacker.totalhp
        print"You are at full health"
        player.potions -=1
    else:
        return "Sorry you are out of potions"
        
def info():  #Player Info
    erase()
    print "Name:",player.name
    print "HP:", player.hp
    print "Attack:", player.attack
    print "Total Potions:", player.potions
    print "Level:", player.lvl
    print "Exp:", player.exp
    print "Total Kills:", player.totalwins
    menu()
    
def combat():  #Puts player into Combat
    goblin=names[randint(0, len(names)-1)]   #Getting Random Goblin Name
    name=goblin
    goblin=Goblin()   #Making Goblin
    
    while player.hp>0 and goblin.hp>0:   #Combat
        erase()
        print "%s's Turn" % player.name
        attack(player, goblin)
        if goblin.hp>0:
            print "\n"
            print "%s The Goblin's Turn" % name
            attack (goblin, player)
            print "\n \n"
            print "Your HP is", player.hp
            def decision():
                print "Press ENTER to attack again."
                print "(2) Run Away"
                print "(3) Heal"
                answer()
            def answer():
                answer=raw_input(">")
                if answer=="2":
                    print "You Ran Away"
                    menu()
                elif answer=="3":
                    heal(player)
                    print "Your HP is", player.hp
                    decision()
            decision()
        else:
            print "Your HP is", player.hp
            print "player defeated %s the Goblin" % name
            player.rest+=1 #rest timer
            player.totalwins +=1 #total wins
            player.exp +=2 #gain exp
            player.nextlevel-=2 #progress towards level
            print "You gain 2 exp"
            if randint(1,5)==3: #find potions?
                print "You found a potion!"
                player.potions+=1
            if player.nextlevel <=0:
                levelup()
                menu()
            else:
                menu()
    
def answer(): #Decision Maker
    answer=raw_input(">")
    if answer=="1":
        combat()
    elif answer=="2":
        info()
    elif answer=="3":
         rest()
    else:
        print "Sorry Something Went Wrong, Please Contact Developer"
        
    
def menu(): #Main Menu
    print """
    (1) Combat
    (2) Player Info
    (3) Rest
    """
    answer()

def startup():
    print"Welcome To Goblin Attack"
    player.name=raw_input("What is your name? >")    
    menu()
    
startup()