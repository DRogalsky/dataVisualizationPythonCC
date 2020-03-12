from random import randint

class Die:
    "a class to represent a single die"

    def __init__(self, num_sides=6):
        """assume 6 sides"""
        self.num_sides = num_sides

    def roll(self):
        """spit out a random number between 1 and the number of sides"""
        return randint(1, self.num_sides)
