import random

"""
reference: https://stackoverflow.com/questions/45069085/dice-roller-for-python
"""


def main():
    rolls = get_rolls()
    dice = get_dice()
    sides = get_sides()

    nrolls = 1
    for r in range(rolls):
        roll = []
    for d in range(dice):
        roll.append(random.randint(1, sides))
    print('Roll -', nrolls, ':', *roll)
    nrolls += 1


def get_rolls():
    rolls = int(input('Enter the number of rolls: '))
    while rolls <= 0:
        print('Number of rolls must be higher than 0')
        rolls = int(input('Enter the number of rolls: '))
    return rolls


def get_dice():
    dice = int(input('Enter the number of dice being rolled: '))
    while dice < 1 or 5 < dice:
        print('Number of dice being rolled must be between 1 and 5')
        dice = int(input('Enter the number of dice being rolled: '))
    return dice


def get_sides():
    sides = int(input('Enter the number of sides on the dice: '))
    while sides < 2 or 36 < sides:
        print('Number of sides on dice must be between 2 and 36')
        sides = int(input('Enter the number of sides on the dice: '))
    return sides


main()
