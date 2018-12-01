import random, time

def text(words):
    for i in words:
        print(i,end='',flush=True)
        time.sleep(0.02)
    print()
class main():
    def __init__(self):
        print("What is your name ?")
        self.name = "test subject"
        text("What is your job ?\n1-Timber\n2-Drunk\n3-Merchant")
        while True:
            try:
                move = int(input())
            except:
                print("Wrong input!")
            if move == 1:
                self.stealth = 1
                self.strength = 3
                self.intelligent = 2
                self.axe = True
            if move == 2:
                self.stealth = 3
                self.strength = 1
                self.intelligent = 2
                self.bottle = True
            if move == 3:
                self.stealth = 2
                self.strength = 1
                self.intelligent = 3
                self.money = True
            break
            self.hp = 20 + 5 * strength
player = main()  

def questZero():
    text("köpek saldırır")
    text("1-Attack the Wolf\n2-Sneak around\n3-Calm the wolf")
    chance = random.randint(1,101)
    while True:
        try:
            move = int(input())        
            if move == 1:
                if player.strength * 25 > chance:
                    text("You win")
                    questOne()
                else:
                    text("öldün")
            if move == 2:
                if player.stealth * 25 > chance:
                    text("sneak")
                    questOne()
                else:
                    text("öldün")
            if move == 3:
                if player.intelligent * 25 > chance:
                    text("")

        except:
            pass

def questOne():
    pass

def questTwo():
    pass

questZero()



        
