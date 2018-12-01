import random, time

def type(words):
    for i in words:
        print(i,end='',flush=True)
        time.sleep(0.02)
        print()

class player():
    def __init__(self):
        print("What is your name ?")
        self.name = input()
        type("What is your job ?\n1-Timber\n2-Drunk\n3-Merchant")
        while True:
            try:
                move = input()
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
    
def questZero():
    type("köpek saldırır")
    while True:
        try:
            move = input()        
            if move == 1:

def QuestOne():
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

def QuestTwo():
    type("


firstStory()
        
