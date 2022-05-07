from classes.ninja import Ninja
import random

class Superninja(Ninja):
    def __init__( self , name ):
        super().__init__(name)

    def attack(self, pirate):
        if(random.randint(1,5) == 5):
            if Ninja.can_attack(self.health):
                print("Special attack!")
                pirate.health -= ((random.randint(1,15) + self.strength ) * 2) - pirate.speed
        else:
            super().attack(pirate)
        return self