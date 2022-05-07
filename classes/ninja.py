import random
class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        if Ninja.can_attack(self.health):
            pirate.health -= (random.randint(1,15) + self.strength - pirate.speed)
        else:
            print(f"{self.name} is dying and cannot attack.")
        return self

    def die (self):
        print(f"{self.name} has died.")

    @staticmethod
    def can_attack(health):
        if health <= 0:
            return False
        else:
            return True