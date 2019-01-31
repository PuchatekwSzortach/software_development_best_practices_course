"""
Module with advanced stuff
"""

import basic


class Warrior(basic.Person):

    def __init__(self, name, age, strength):

        super().__init__(name, age)
        self.strength = strength
