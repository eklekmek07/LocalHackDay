class mob():
	def __init__(self,name,battlecry,quote,deathrattle,laugh,difficulty):
		self.name = name
		self.battlecry = battlecry
		self.quote = quote
		self.deathrattle = deathrattle
		self.laugh = laugh
		self.difficulty = difficulty
	
	def combat(self):
		text("Fight begin with {}".format(self.name))
		target = randint(1,self.difficulty)
		lives = player.strength + 3



def combat(difficulty, name, battlecry, quote, deathrattle, laugh):

    
    text(name + " : " + battlecry + "\n")
    
    number = difficulty * 10
    kill = random.randint(1, number)
    lives = player.strength + 4
    accuracy = number*2
    
    print("Move cursor to choose О to attack and find the kill spot, you have " + str(lives) + " lives.")
    while True:
        a = random.randint(0,accuracy*2) - accuracy
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
        
        print("Lives: " + str(lives))
        if (lives <= 0):
            text(name + " : " + laugh + "\n")
            return False
        
        text(name + " : " + quote[random.randint(0,len(quote)-1)] + "\n")