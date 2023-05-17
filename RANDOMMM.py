import random


class Dice:
    def roll():
        dice1 = [1,2,3,4,5,6]
        dice2 = [1,2,3,4,5,6]
        r1 = random.choice(dice1)
        r2 = random.choice(dice2)
        rt = (r1,r2)
        print(rt)



for i in range(6):
    Dice.roll()
    Dice.roll()
    Dice.roll()
    Dice.roll()

