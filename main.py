import random

user_points = 0
computer_points = 0


def roll_the_dice():
    '''
    Function roll_the_dice simulates throwing two six-sided dice.
    :return: the amount of throws, type - int
    '''
    roll_twice = []
    for _ in range(2):
        roll = random.randint(1, 6)
        roll_twice.append(roll)
    return sum(roll_twice)


def game():
    pass


# if __name__ == '__main__':
#     game()
