from classes.ninja import Ninja
from classes.pirate import Pirate
from classes.superninja import Superninja
from classes.superpirate import Superpirate


michelangelo = Superninja("Michelangelo")

jack_sparrow = Superpirate("Jack Sparrow")

while (michelangelo.health > 0 and jack_sparrow.health > 0):
    michelangelo.attack(jack_sparrow)
    jack_sparrow.show_stats()
    jack_sparrow.attack(michelangelo)
    michelangelo.show_stats()
if (michelangelo.health <= 0):
    michelangelo.die()
else:
    jack_sparrow.die()

"""
# Options for project extension: allow each instance of a ninja or pirate to be appended to list of such,
allowing for parties of multiple ninjas and multiple pirates to fight against each other.
"""