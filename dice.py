import random
class Dice():

    #no attributes that I can think of
    def __init__(self):
        pass

    #returns a number between 1 and 6
    def roll(self):
        return random.randint(1,6)

    #returns a list with 5 numbers between
    #1 and 6
    def set_rolls(self):
        i = 0
        rolls = []
        while i != 5:
            if i != 5:
                outcome = self.roll()
                rolls.append(outcome)
                i += 1
        return rolls