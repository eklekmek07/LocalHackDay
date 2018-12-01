import random
from time import sleep as wait

def tp(text, time = 0.04):
    """type writer effect"""
    for i in text:
        print(i,end="",flush= True)
        wait(time)
    print("")

def check():
    if player.alive or enemy.alive == False:
        return 

class character():
    def __init__(self, hp, strength, agility, defence, intelligent, name, Aİ = False):
        self.name = name
        self.alive = True
        self.Aİ = Aİ
        self.target = None
        self.stance = 1 # 0=Sleep 1=Starting 2=Block
        self.base_hp = hp
        self.hp = hp
        self.base_strength = strength
        self.strength = strength
        self.defence = defence
        self.base_defence = defence
        self.base_agility = agility
        self.agility = agility
        self.base_energy = 10 + round((strength+agility)/2)
        self.energy = self.base_energy
        self.life_steal = False
        self.intelligent = intelligent
        self.base_intelligent = intelligent
        self.turn = False
        self.life_steal_turn = 0
        self.player_xp = 4
        
    def choose_target(self):
        """choose what to hit"""
        if self.Aİ == True:
            self.target = player
        else:
            self.target = enemy # add switch beetwen enemies.. 

    def on_enemy_death(self):
        print("{} has died.".format(enemy.name))
        low = self.player_xp - 3
        high = self.player_xp + 3
        enemy.base_strength = random.randint(low,high)
        enemy.base_agility = random.randint(low,high)
        enemy.base_defence = random.randint(low,high)
        enemy.base_intelligent = random.randint(low,high)
        enemy.base_hp = random.randint(low,high) * 4
        enemy.strength, enemy.agility, enemy.defence, enemy.intelligent, enemy.hp = enemy.base_strength, enemy.base_agility, enemy.base_defence, enemy.base_intelligent, enemy.base_hp
        enemy.stance = 1
        enemy.alive = True
        
    def show_stats(self):
        print("Name:{}\nHitpoint:{}/{}\nEnergy:{}/{}\nStrength:{}\nAgilty:{}\nDefence:{}\nİntelligent:{}".format(self.name,self.hp,self.base_hp,self.energy,self.base_energy,self.strength,self.agility,self.defence,self.intelligent))       

    def check(self):
        if self.hp <= 0:
            self.alive = False
        if self.turn == False:
            self.strength = self.base_strength
            self.agility = self.base_agility
            self.defence = self.base_defence
            self.intelligent = self.base_intelligent
        if self.life_steal_turn < 1:
            self.life_steal = False

    def move(self):
        attack = " Attack"
        block = " Block" #fear 
        sleep = " Sleep" #poisoned or something like that
        special = " Special"
        if self.energy < 10:
            special = " ̶s̶p̶e̶c̶i̶a̶l̶"
        if self.energy < 4:
            attack = " ̶a̶t̶t̶a̶c̶k̶"
        print("Your energy:{}/{}".format(self.energy,self.base_energy))
        print("Choose your move:\n1-{} %{} hit chance\n2-{} \n3-{}\n4-{}".format(attack,self.hit_percentenge(),block,sleep,special))
        choice = None
        while choice == None:
            try:
                choice = int(input("Your choice:"))
                if not 0 < choice < 5:
                    raise ValueError
            except:
                print("Only enter the number please")
            if choice == 1: 
                if self.energy > 3:
                    self.attack(self.target)
                else:
                    print("You are too tired to attack")
                    choice = None
            elif choice == 2:
                self.block()
            elif choice == 3:
                self.sleep()
            elif choice == 4:
                if self.energy > 9:
                    self.special()
                else:
                    print("You are too tired to do special ability")
                    choice = None 

    def hit_chance(self, target):
        """To decide to can hit target or not"""
        if (self.agility - target.agility + 20) * 2.5 > random.randint(1,101):
            return True
        else:
            return False

    def hit_percentenge(self):
        count = 0
        for i in ['x' * 100]:
            if self.hit_chance(self.target) == True:
                count += 1
        return count
   
    def attack(self, target):
        hit = self.hit_chance(target)
        dmg = self.strength - round(target.defence * 1/2)
        if dmg <= 0:
            tp("{} tickled => {}".format(self.name, target.name))
        else:
            if hit and self.life_steal == True:
                if self.hp + round(dmg * 0.4) > self.base_hp:
                    heal = self.base_hp - self.hp
                    self.hp = self.base_hp
                else:
                    heal = round(dmg * 0.4)
                    self.hp += heal
                tp("{} {} life stole".format(self.name, heal))
            if hit == True:
                target.hp -= dmg
                tp("{} gives {} damage to {}".format(self.name,dmg,target.name))
            else:
                tp("{} missed".format(self.name))
        self.energy -= 4
    
    def special(self):
        dice = random.randint(0,15)
        if dice < 5:
            self.life_steal_turn = random.randint(2,5)
            tp("{} can steal life for {} turn".format(self.name,self.life_steal_turn))
            self.life_steal = True
        elif dice < 15:    
            self.defence = 50
            tp("{} has protection for 1 turn".format(self.name))
        else:
            dmg = round(self.strength * 2.5)
            self.target.hp -= dmg
            print("{} struck by lightning (-{})".format(self.target.name,dmg)) 
        self.energy -= 10

    def block(self):
        self.defence = round(self.defence * 2/3)
        self.energy += round(self.base_energy * 1/3)
        self.turn = False
        self.target.turn = True
        self.stance = 2
    
    def sleep(self):
        self.agility = round(self.base_agility * 1/3)
        self.energy += round(self.base_energy * 2/3)
        self.turn = False
        self.target.turn = True
        self.stance = 1

enemy = character(20, 2, 3, 1, 1,"ToprakT", True)
player = character(20, 10, 3, 1, 1, "Umut")
player.choose_target()
enemy.choose_target()

def in_game_stats():
    print("----------\n{} {}/{}\n{} {}/{}\n----------".format(player.name,player.hp,player.base_hp,enemy.name,enemy.hp,enemy.base_hp))

def enemy_ai():
    energy = enemy.energy / enemy.base_energy * 10
    chance = random.randint(1,10)
    if energy > chance and enemy.energy > 3:
        print("Attack")
        enemy.attack(enemy.target)
    elif energy < chance and enemy.energy > 9:
        print("Special")
        enemy.special()
    elif energy < chance and enemy.energy < 10:
        print("Block")
        enemy.block()
    elif energy < chance and enemy.energy < 10:
        print("Sleep")
        enemy.sleep()
    else:
        print("Nothing")

def enemy_maker():#planned (will be listed enemy)
    pass

def target_chooser():#auto
    player.target = enemy
    enemy.target = player
    
def duel():
    if random.randint(0,1) == 1:
        player.turn = True
        print("{} starts first..".format(player.name))
    else:
        enemy.turn = True
        print("{} starts first..".format(enemy.name))
    while True:
        while player.turn and player.alive == True and enemy.alive == True:
            player.move()
            player.check()
            enemy.check()
            in_game_stats()
        while enemy.turn:
            enemy_ai()
            player.check()
            enemy.check()
            in_game_stats()
        if player.alive == False:
            print("Game Over")
            break
        if enemy.alive == False:
            player.on_enemy_death()
            target_chooser()   
duel()

