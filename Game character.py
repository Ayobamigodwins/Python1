           

print("Welcome to the Game Character Class!")

print ("----------------------------------------------------------------")

class MyCharacter:
    def __init__(self, name, health, shield, strength, attack_power):
    
        self.name = name
        self.health = health
        self.shield = shield
        self.strength = strength
        self.attack_power = attack_power
    def attack(self):
        self.attack = self.strength + self.attack_power
       
    def defence(self):

        self.defence = self.shield + self.health
    def total_power(self):
        self.total_power = self.attack + self.defence
    
            
        


class OponentCharacter:
    def __init__(self, name1, health1, shield1, strength1, attack_power1):
        
        self.name1 = name1
        self.health1 = health1
        self.shield1 = shield1
        self.strength1 = strength1
        self.attack_power1 = attack_power1
    def attack1(self):
        self.attack1 = self.strength1 + self.attack_power1
        
    def defence1(self):
        self.defence1 = self.shield1 + self.health1
    def total_power1(self):
        self.total_power1 = self.attack1 + self.defence1
        

character = input("Enter the name of your character: ")  
opponent = input("Enter the name of your opponent: ")  
MyPlayer = MyCharacter(character, 100, 50, 20, 10)
MyOpponent = OponentCharacter(opponent, 80, 15, 5, 10)


       

 
        

   
print(MyPlayer.name, "has health:", MyPlayer.health, "shield:", MyPlayer.shield, "strength:", MyPlayer.strength, "attack power:", MyPlayer.attack_power)
print(MyOpponent.name1, "has health:", MyOpponent.health1, "shield:", MyOpponent.shield1, "strength:", MyOpponent.strength1, "attack power:", MyOpponent.attack_power1)  
MyPlayer.attack()
MyPlayer.defence()
MyPlayer.total_power()
MyOpponent.attack1()
MyOpponent.defence1()
MyOpponent.total_power1()
print(f"{MyPlayer.name} total attack power is {MyPlayer.attack}")
print(f"{MyPlayer.name} total defense is {MyPlayer.defence}")   
print(f"{MyOpponent.name1} total attack power is {MyOpponent.attack1}")
print(f"{MyOpponent.name1} total defense is {MyOpponent.defence1}")
print(f"{MyPlayer.name} total power is {MyPlayer.total_power}")
print(f"{MyOpponent.name1} total power is {MyOpponent.total_power1}")

print("Let the battle begin!") 

