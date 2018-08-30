import random

class Dice:

    def __init__(self):
        return

    def roll(self):
        reroll = "yes"
        while reroll != "no":
            print(random.randint(1, 6))
            print('\n')
            reroll = input('Roll again? (yes/no)')
        return

x = Dice()
x.roll()
