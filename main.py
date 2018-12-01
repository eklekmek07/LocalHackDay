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
        text("What is your job ?\n1-Timber\n2-Drunk\n3-Merchant")
        move = input_handler()
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

def questZero():
    text("köpek saldırır")
    text("1-Attack the Wolf\n2-Sneak around\n3-Calm the wolf")
    chance = random.randint(1,101)
    move = input_handler()       
    if move == 1:
        if player.strength * 25 > chance:
            text("You win")
            questOne()
        else:
            text("öldün")
    if move == 2:
        if player.stealth * 25 > chance:
            text("sneak")
        elif player.strength * 25 > chance:
            text("He noticed and attacked you but you fought better.He is dead.")
            questTwo()
        else:
            text("YOU DIED")
    if move == 3:
        if player.intelligent * 25 > chance:
            text("calm")
            text("Dog bring you a stick")
            player.stick = True
            questOne()
        else:
            text("köpek saldırır")

def questOne()
    text("You see a ruined bridge")
    text("1-Try to fix it\n2-Try to swim\n3-Try to pass anyway")
    chance = random.radnint(1,101)
    move = input_handler()
    if move == 1:
        if player.strength 
def questTwo():
    text("You see an Orc")
    text("1-Attack the Orc!\n2-Sneak around\n3-Talk with him")
    chance = random.randint(1, 101)
    move = input_handler()
    if move == 1:
        if player.strength * 20 > chance:
            text("You have won the battle!")
            questTwo()
        else:
            text("YOU DIED")
    if move == 2:
        if player.stealth * 40 > chance:
            text("You have successfully sneaked around him")
            questTwo()
        elif player.strength * 20 > chance:
            text("He noticed and attacked you but you fought better.It is dead.")
            questTwo()
        else:
            text("YOU DIED")
        if move == 3:
            if player.intelligent * 40 > chance:
                text("You have gained his trust")
                player.stick = True
                questTwo()
            elif player.strength * 20 > chance:
                text("He got angry and attacked you but you fought better.It is dead.")
                questTwo()
            else:
                text("YOU DIED")
def questTwo():
    pass

def questThree():
    text("You saw mountains in the distance and decide to go there")
    #minator event
    text("On the road you saw a Minatour")
    text("1-Attack him\n2-Sneak Around\n3-Distract him")
    move = input_handler()


questZero()



        
