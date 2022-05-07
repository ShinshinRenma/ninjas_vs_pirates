from classes.pirate import Pirate
import random

class Superpirate(Pirate):
    def __init__( self , name ):
        super().__init__(name)

    def attack(self, ninja):
        if(random.randint(1,5) == 5):
            if Pirate.can_attack(self.health):
                print("Special attack!")
                ninja.health -= ((random.randint(1,10) + self.strength ) * 2) - ninja.speed
        else:
            super().attack(ninja)
        return self