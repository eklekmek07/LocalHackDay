from time import sleep
from random import randint
import graphic

def text(words,duration = 0.02):
    for i in words:
        print(i,end='',flush=True)
        sleep(duration)
    print()

def restartGame():
    print("Do you want to play again ?")
    move = input("y/n:")
    if move == "y":
        del player
        player = main()
        questZero()
    else:
        quit()

def death():
    graphic.game_over()
    print("You died")
    restartGame()

def win():
    print("Congratulations")
    text("You took your mom's revenge...")
    restartGame()

def funny_death():
    text("Well thats too bad you press wrong button :')")
    death()

def combat(difficulty, name, battlecry, quote, deathrattle, laugh):
    text("{}: {}".format(name,battlecry))
    number = difficulty * 10
    kill = randint(1, number)
    lives = player.strength + 4
    accuracy = number*2
    print("Move cursor to choose О to attack and find the kill spot, you have {} lives.".format(lives))
    while True:
        a = randint(0,accuracy*2) - accuracy
        for i in range(1,number):          
            if(abs(kill-i+a)<=accuracy):
                print("О", end = '', flush = True)
            else:
                print("●", end = '', flush = True)
        print()
        
        place = input()
        if(place == "a"):
            lives += 5                                                                
        attack = len(place) + 1
        
        miss = abs(attack-kill)

        if(miss==0):
            text(name + " : " + deathrattle + "\n")
            return True
        else:
            if(miss%2==1):
                accuracy = miss
            else:
                accuracy = miss + 1
        
        lives-=1
        
        print("Lives: {} ".format(lives))
        if (lives <= 0):
            text("{}: {}".format(name,laugh))
            death()
        text(name + " : " + quote[randint(0,len(quote)-1)] + "\n")

def input_handler():
    while True:
        try:
            a = int(input())
            return a
        except ValueError:
            print("Wrong Input!")

class main():
    def __init__(self):
        print("What is your name ?")
        self.name = input()
        text("You are a...\n1-Timber\n2-Drunk\n3-Merchant")
        move = input_handler()
        self.money = False
        self.axe = False
        self.bottle = False
        self.timber = False
        self.merchant = False
        self.drunk = False
        self.mud = False
        self.torch = False        
        if move == 1:
            self.stealth = 1
            self.strength = 3
            self.intelligent = 2
            self.axe = True
            self.timber = True
        if move == 2:
            self.stealth = 3
            self.strength = 1
            self.intelligent = 2
            self.bottle = True
            self.drunk = True
        if move == 3:
            self.stealth = 2
            self.strength = 1
            self.intelligent = 3
            self.money = True
            self.merchant = True
text("You woke up in the dark forest. Gradually, you remembered what happened.\nThe evil vampire had drunk your mothers blood and had caused her death.\nNow, you have an enormous grudge to the evil vampire.\nYou have to find the vampire and have to defeat her to death.")
player = main()  

def questStart():
    player = main()
    
def questZero():#wolf
    text("You see an angry wolf.")
    text("1-Attack the Wolf!\n2-Sneak around\n3-Calm the wolf")
    chance = randint(1,101)
    move = input_handler()       
    if move == 1:
        combat(2, "Wolf", "Aaauuuuuuw", ["Woof!", "Grrrrrrr", "Woof Woof!!"], "woof...", "Grrrrr WOOOF!")
        text("He noticed and attacked you but you fought better.")
        text("He is dead.You continued on your path.")           
        questOne()       
    if move == 2:
        if player.stealth * 25 > chance or player.drunk == True:
            text("You have successfully sneaked around it and continued on your path.")
            questOne()
        elif player.strength * 25 > chance:
            #duel
            text("you couldn't sneak past.")
            if(combat(2, "Wolf", "Aaauuuuuuw", ["Woof!", "Grrrrrrr", "Woof Woof!!"], "woof...", "Grrrrr WOOOF!")):
                text("He noticed and attacked you but you fought better.")
                text("He is dead. You continued on your path.")
            else:
                death()
            questOne()
    if move == 3:
        if player.intelligent * 25 > chance:
            text("The wolf calmly waged its tail.It likes you.")
            graphic.wolf_with_stick()
            move = input("y or n:\n")
            if move == "y":
                player.stick = True            
                text("You put it in your bag and continued on your path.")
                questOne()
            else:
                player.stick = False
                text("You left it and continued on your path.")
            questOne()            
        else:
            text("Wolf bit your hand and startet attacking you")   
            if(combat(2, "Wolf", "Aaauuuuuuw", ["Woof!", "Grrrrrrr", "Woof Woof!!"], "woof...", "Grrrrr WOOOF!")):
                text("He noticed and attacked you but you fought better.")
                text("He is dead.You continued on your path.")
                questOne()
            else:
                death() 
        questOne()
    else:
        funny_death()  
            

def questOne():#bridge
    text("You see a bridge over the river but there are men in front of it,they ask for money")
    if player.money == True:
        text("Do you want to give money ?")
        move = input("y or n:\n")
        if move == "y":
            text("You passed and continued on your path.")
            text("You no longer have money.")
            player.money == False                                                                                                                                                                                                
            questTwo()
    else:
        text("You don't have any money. You're not a merchant.")
    if player.timber == True:
        text("Luckily, you know how to build a bridge. Do you want to buil a bridge?")        
        move = input("y or n:\n")
        if move == "y":
            text("You made a bridge")
            text("You continued on your path.")
            questTwo()
    text("Shaggy men stare at you angrily.")                                                
    text("1-Fight them\n2-Swim\n3-Sneak pass them")
    chance = randint(1,101)
    move = input_handler()
    if move == 1:
        
        #duel
        text("The brawl has begun!")
        if(combat(3, "Men", "You think you're so strong!", ["You think you can defeat us?", "Give up!", "We like to fight!"], "You chated!", "Ha ha ha HAHAHAHAH!")):
            text("You attacked the men and barely won.")
            text("You continued on your path.")
        else:
            death() 
        questTwo()
       
    if move == 2:
        text("You have barely swam to the other side but you are wet now.")
        text("You continued on your path.")
        player.wet = True
        questTwo()
    if move == 3:
        if player.stealth * 30 > chance:
            text("You managed to distrack them and pass.")
            text("You continued on your path.")
            questTwo()
        else:
            text("You could not distrack them.They noticed and attacked you!")
            #duel
            if(combat(3, "Men", "You snobby men!", ["You think you can defeat us?", "Give up!", "We like to fight!"], "You chated!", "Ha ha ha HAHAHAHAH!")):
                text("You attacked the men and barely won.")
                text("You continued on your path.")
            else:
                death()            
            questTwo()                    
                                    
        
def questTwo():#orc
    text("You spot an enormus orc!!")
    sleep(1)        
    graphic.orc()
    text("1-Attack the Orc!\n2-Sneak around\n3-Talk with him")
    chance = randint(1, 101)
    move = input_handler()
    if move == 1:
        if(combat(4, "Orc", "WAAAAAGGHHH!", ["Me a big 'un", "I eat humans like you for breakfast", "I fight fo' fun"], "You were lucky!", "GG EZ")):
                text("You attacked the orc and nearly died.")
                text("You continued on your path.")
                questThree()
        else:
            death()        
    if move == 2:
        if player.stealth * 40 > chance:
            text("You have successfully sneaked around him.")
            sleep(0.7)
            text("You continued on your path.")                  
            questThree()
        combat(4, "Orc", "WAAAAAGGHHH!", ["Me a big 'un", "I eat humans like you for breakfast", "I fight fo' fun"], "You were lucky!", "GG EZ")
        text("You attacked the orc")
        text("You continued on your path.")
        questThree()
        death()
    if move == 3:
        if player.intelligent * 40 > chance:
            text("You have gained his trust")
            text("You continued on your path.")
            questThree()
        #duel
        if(combat(4, "Orc", "WAAAAAGGHHH!", ["Me a big 'un", "I eat humans like you for breakfast", "I fight fo' fun"], "You were lucky!", "GG EZ")):
            text("You attacked the orc and nearly died.")
            text("You continued on your path.")
            questThree()
        else:
            death()

def questThree(): #minator
    text("You saw the mountain before your village.You are close.")
    sleep(1)
    graphic.minotor()
    text("What do you want to do?")    
    text("1-Attack him\n2-Sneak Around\n3-Distract him")
    move = input_handler()
    chance = randint(0,101)
    if move == 1:
        text("You decided to fight!")
        if(combat(5, "Minataur", "Me axe is bigger than you", ["Ye are a puny human", "I will crush ye!!!", "AAAHHHH!!"], "Me dont wanna be burger!", "Yer the beef now!!")):
                text("You attacked the minatour and somehow won")
                text("You continued on your path.")
                questFour()
        else:
            death()                                    
        #duel
    if move == 2:
        if player.stealth * 25 < chance:
            text("You have managed to sneak around him.")
            text("You continued on your path.")
            questFour()            

        else:
            text("It noticed and attacked you!")            
            if(combat(5, "Minataur", "Ye look like ye about to die", ["Ye are a puny human", "I will crush ye!!!", "AAAHHHH!!"], "Me dont wanna be burger!", "Yer the beef now!!")):
                text("You attacked the minatour and somehow won.")
                text("You continued on your path.")
                questFour()
            else:
                death()                                                            
    if move == 3:
        text("You decided to throw something to distract")
        if player.drunk == True or player.intelligent * 25 > chance:
            text("You have successfully distracted it.")            
            text("What do you want ?\n1-Walk past\n2-Back Stab")
            move = input_handler()
            if move == 1:
                text("You continued on your path.")
                questFour()
            elif move == 2:
                #duel avantajlı
                text("you weakened the enemy")                                
                if(combat(3, "Minataur", "Me axe is bigger than yours", ["Ye are a puny human", "I will crush ye!!!", "AAAHHHH!!"], "Me dont wanna be burger!", "Yer the beef now!!")):
                    text("You attacked the minatour and somehow won")
                    text("You continued on your path.")
                else:
                    death()
            else:
                funny_death()
    
def questFour():#vampir
    text("As the road continues you reach the mountain. There is a cave near it.")
    if player.torch and player.stick == True:
        text("Do you want to make a Torch(use stick and firestone) ?")
        move = input("y/n:")
        if move == "y":
            player.stick = False            
            player.firestone = False
            player.stealth += 1
            player.strength -= 1
            player.torch = True
        if move == "n":
            pass
        else:
            funny_death()
    text("Entering the cave...")
    graphic.vampire()
    if player.torch == True:
        player.strength += 1
        text("What do you want to do ?\n1-Attack him\n2-Sneak Attack\n3-Throw torch to him")
    else:
        text("What do you want to do ?\n1-Attack him\n2-Sneak Attack")
    move = input_handler()
    chance = randint(0,100)            
    if move == 1:
        text("You attacked him for your life.")                            
        if(combat(6, "Vampire", "I will suck you dry!!", ["You smell delicious", "You look very tasty", " I love blood!!"], "Fool, I will come back!", "You had no hope...")):
            text("He noticed and attacked you but you fought better.")
            text("He is dead.You continued on your path.")
            win()
        else:
            death()
    elif move == 2:
        if player.mud == True:
            text("You managed to hide your body heat with mud")
            if(combat(6, "Vampire", "I will suck you dry!!", ["You smell delicious", "You look very tasty", " I love blood!!"], "Fool, I will come back!", "You had no hope...")):
                text("He noticed and attacked you but you fought better.")
                text("He is dead.You continued on your path.")
                win()
            else:
                death()
        else:
            if player.stealth * 25 > chance:
                text("You sneaked behind the vampire")
                if(combat(5, "Vampire", "I will suck you dry!!", ["You smell delicious", "You look very tasty", " I love blood!!"], "Fool, I will come back!", "You had no hope...")):
                    text("He noticed and attacked you but you fought better.")
                    text("He is dead.You continued on your path.")
                    win()
                else:
                    death()                
            else:
                
                if(combat(7, "Vampire", "I will suck you dry!!", ["You smell delicious", "You look very tasty", " I love blood!!"], "Fool, I will come back!", "You had no hope...")):
                    text("He noticed and attacked you but you fought better.")
                    text("He is dead.You continued on your path.")
                    win()
                else:
                    death()
    elif move == 3 and player.torch == True:
        if player.intelligent * 25 > chance:
            player.strength += 1
            text("Vampire got scared of the fire, she is weakened. Your morale increased (+1 life)")
            if(combat(5, "Vampire", "I will suck you dry!!", ["You smell delicious", "You look very tasty", " I love blood!!"], "Fool, I will come back!", "You had no hope...")):
                text("She noticed and attacked you but you fought better.")
                text("She is dead.You continued on your path.")
                win()
            else:
                death()
        else:
            player.strength -=1
            player.torch = False
            if(combat(6, "Vampire", "I will suck you dry!!", ["You smell delicious", "You look very tasty", " I love blood!!"], "Fool, I will come back!", "You had no hope...")):
                text("She noticed and attacked you but you fought better.")
                text("She is dead.You continued on your path.")
                win()
            else:
                death()
    else:
        funny_death()

questZero()



        
