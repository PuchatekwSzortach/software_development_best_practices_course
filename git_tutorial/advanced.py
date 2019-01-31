"""
Module with advanced stuff
"""
import random

import random

import basic


class Warrior(basic.Person):

    def __init__(self, name, age, strength):

        super().__init__(name, age)
        self.strength = strength

    def __repr__(self):

        basic_representation = super().__repr__()
        return basic_representation + ", strength level {}".format(self.strength)

    def punch(self):

        punch_strength = random.randint(0.2 * self.strength, 0.8 * self.strength)
        return "{} punching with strength {}!".format(self.name, punch_strength)

    def kick(self):

        kick_strength = random.randint(0.5 * self.strength, self.strength)
        return "{} kicking with strength {}!!!".format(self.name, kick_strength)
