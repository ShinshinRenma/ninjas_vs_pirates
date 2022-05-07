import random
class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , ninja ):
        if Pirate.can_attack(self.health):
            ninja.health -= (random.randint(1,10) + self.strength - ninja.speed)
        else: 
            print(f"{self.name} is dying and cannot attack.")
        return self

    def die(self):
        print(f"{self.name} has died.")

    @staticmethod
    def can_attack(health):
        if health <= 0:
            return False
        else:
            return True

