"""
Module with advanced stuff
"""

import basic


class Warrior(basic.Person):

    def __init__(self, name, age, strength):

        super().__init__(name, age)
        self.strength = strength

    def __repr__(self):

        basic_representation = super().__repr__()
        return basic_representation + ", strength level {}".format(self.strength)
