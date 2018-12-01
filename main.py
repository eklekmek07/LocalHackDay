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
player = main()  

def questZero():
    text("köpek saldırır")
    text("1-Attack the Wolf\n2-Sneak around\n3-Calm the wolf")
    chance = random.randint(1,101)
    while True:
        try:
            move = int(input())        
            if move == 1:
                print("okey")
                if player.strength * 25 > chance:
                    text("You win")
                    questOne()
                else:
                    text("öldün")
            if move == 2:
                print("aldı")
                if player.stealth * 25 > chance:
                    text("sneak")
                    questOne()
                else:
                    text("öldün")
        except:
            pass

def questOne():
    #check name item
    type("Hikaye başlar.. bla bla dağların arasında uyandın..\n")
    type("Yaşlı Amca:\nMerhaba genç köyümüze hoş geldin falan filan..")
    print("Adınız:")
    player.name = input()
    while True:
        try:
            type("1-Köye git\n2-Ormana git\n3-Dinlen")
            choose = input()
            if choose == 1:
                pass
            elif choose == 2:
                print("Köye gittin")
        except:
            print("Lütfen doğru bir karar giriniz")
        break

def questTwo():
    pass

#questZero()
print("selm")
def hesap():
    chance = random.randint(0,100)
    count = 0
    for i in range(100):
        if player.strength * 25 > chance:
            count += 1
    print(count)
hesap()

        
