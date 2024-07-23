from weapon import fists
class Organism:
    alive = True
    
    def eat(self):
        print("this organism eats")
    
    def breathe(self):
        print("this organism breathes")
        
    def move(self):
        print("this organism moves")
        


        #alot of uncertainties
class Human(Organism):
    malicious = True
    sentient = True
    
    #need to define stats 
    def __init__(self, name:str, health:int, strength:int, agility:int, intelligence:int) ->None:
        self.name = name
        self.health = health
        self.health_max = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.weapon = fists
        #attacker and the target 
    def attack(self, target) -> None:
        damage = self.strength + self.weapon.damage
        target.health -= damage
        target.health = max(target.health, 0)
        
class Hero(Human):
    def __init__(self,
                 name:str,
                 health:int,
                 strength:int,
                 agility:int,
                 intelligence:int)->None:
        super().__init__(name=name, health=health, strength=strength, agility=agility, intelligence=intelligence)
        
class Enemy(Human):
    def __init__(self,
                 name:str,
                 health:int,
                 strength:int,
                 agility:int,
                 intelligence:int)->None:
        super().__init__(name=name, health=health, strength=strength, agility=agility, intelligence=intelligence)