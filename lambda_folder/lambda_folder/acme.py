import random
from random import randint

# Create class
class product:
    """
    Product Class
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        """
        constructor method
        """
        identifier = random.randint(1000000, 9999999) # default
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """
        Method that calculates price divided by weight
        """
        steal = self.price / self.weight # price divided by weight
        if steal < 0.5:
            return(f'Not so stealable...') # less than .5
        if steal >= 0.5 & steal < 1.0:
            return(f'Kinda stealable.') # more than .5 but less than 1.0
        else:
            return(f'Very stealable!') # more than 1.0

    def explode(self):
        """
        calculates the flammability times the weight
        """
        exp = self.flammability * self.weight
        if exp < 10:
            return(f'...fizzle.')
        if exp >= 10 &  exp < 50:
            return(f'...boom!')
        else:
            return(f'...BABOOM!')

# create subclass
class BoxingGlove(product):
    """
    subclass of Product
    """
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        self.identifier = random.randint(1000000, 9999999) # default
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        """
        Override explode method to always say '...its a glove.'
        """
        exp = self.flammability * self.weight
        if exp == exp:
            return(f'...its a glove.')

    def punch(self):
        """
        Punch method
        """
        weigh = self.weight
        if weigh < 5:
            return(f'That tickles.')
        if weigh >= 5 & weigh < 15:
            return(f'Hey that hurt!')
        else:
            return(f'OUCH!')
