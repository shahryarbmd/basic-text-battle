from Organism import Hero,Enemy
import time
#______________________________
hero = Hero(name= "Kael",
              health= 100,
              strength = 5,
              agility= 5,
              intelligence= 10)
#________________________
enemy = Enemy(name= "Bandit",
              health= 50,
              strength = 2,
              agility= 3,
              intelligence= 1)
while True:
    if enemy.health == 0:
        print("\nEnemy Felled")
        break
    
    hero.attack(enemy)
    enemy.attack(hero)
    
    print(f" health of {hero.name}: {hero.health} ",end='')
    
    print(f" health of {enemy.name}: {enemy.health} ",end='\r')    
    time.sleep(0.5)
    
    