import random, time

def text(words):
    for i in words:
        print(i,end='',flush=True)
        time.sleep(0.02)
    print()

def input_handler():
    try:
        a = int(input())
        return a
    except:
        print("Wrong Input!")

class main():
    def __init__(self):
        #print("What is your name ?")
        self.name = "test subject"
        text("You are a...\n1-Timber\n2-Drunk\n3-Merchant")
        move = input_handler()
        self.money = False
        self.axe = False
        self.bottle = False
        self.timber = False
        self.merchant = False
        self.drunk = False
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

player = main()  

def questZero():#wolf
    text("You see an angry wolf.")
    text("1-Attack the Wolf!\n2-Sneak around\n3-Calm the wolf")
    chance = random.randint(1,101)
    move = input_handler()       
    if move == 1:
        if player.strength * 25 > chance or player.timber == True:
            text("You have killed the wolf and continued on your path.")
            questOne()
        else:
            text("YOU DIED")
    if move == 2:
        if player.stealth * 25 > chance or player.drunk == True:
            text("You have successfully sneaked around it and continued on your path.")
        elif player.strength * 25 > chance:
            text("He noticed and attacked you but you fought better.He is dead.You continued on your path.")
            questTwo()
        else:
            text("YOU DIED")
    if move == 3:
        if player.intelligent * 25 > chance:
            text("The dog calmly waged its tail.It likes you.")
            text("Dog bring you a stick")
            text("You put it in your bag and continued on your path.")
            player.stick = True
            questOne()
        elif player.strength * 20 > chance:
                text("He got angry and attacked you but you fought better.It is dead.")
                questThree()
        else:
                text("YOU DIED")

def questOne():#bridge
    text("You see a guarded bridge,they ask for money")
    if player.money == True:
        text("Do you want to pay money ?")
        move = input("t or f:\n")
        if move == "t":
            text("You passed")
            questTwo()
    if player.timber == True:
        text("Luckily, you know how to build a bridge.")        
        move = input("t or f:\n")
        if move == "t":
            text("You made a bridge")
            questTwo()
    text("1-Fight them\n2-Swim\n3-Sneak pass them")
    chance = random.randint(1,101)
    move = input_handler()
    if move == 1:
        if player.strength * 20 > chance or player.timber == True:
            text("fix bridge")
        else:
            text("fall to the water")
            player.wet = True
    if move == 2:
        pass
        
def questTwo():#orc
    text("You see an Orc")
    text("1-Attack the Orc!\n2-Sneak around\n3-Talk with him")
    chance = random.randint(1, 101)
    move = input_handler()
    if move == 1:
        if player.strength * 20 > chance:
            text("You have won the battle!")
            questThree()
        else:
            text("YOU DIED")
    if move == 2:
        if player.stealth * 40 > chance:
            text("You have successfully sneaked around him")
            questThree()
        elif player.strength * 20 > chance:
            text("He noticed and attacked you but you fought better.It is dead.")
            questThree()
        else:
            text("YOU DIED")
        if move == 3:
            if player.intelligent * 40 > chance:
                text("You have gained his trust")
                player.stick = True
                questThree()
            elif player.strength * 20 > chance:
                text("He got angry and attacked you but you fought better.It is dead.")
                questThree()
            else:
                text("YOU DIED")

def questThree(): #minator
    text("You saw mountains in the distance and decide to go there")
    #minator event
    text("On the road you saw a Minatour")
    text("1-Attack him\n2-Sneak Around\n3-Distract him")
    move = input_handler()

def questFour():#vampir
    text
def sideGoats():
    pass

def 

questZero()



        
