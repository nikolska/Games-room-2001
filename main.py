import random


def user_roll_the_dice():
    '''
    Function simulates rolling two six-sided dice.
    :return: the amount of rolls, type - int
    '''
    print('Press ENTER to roll the dice')
    input()
    roll_twice = [random.randint(1, 6), random.randint(1, 6)]
    return sum(roll_twice)


def comp_roll_the_dice():
    '''
    Function simulates rolling two six-sided dice.
    :return: the amount of rolls, type - int
    '''
    roll_twice = [random.randint(1, 6), random.randint(1, 6)]
    return sum(roll_twice)


def game():
    '''
    The main function of the game "2001".
    :user_points type: int
    :computer_points type: int
    '''
    user_points = 0
    computer_points = 0
    while user_points < 2001 or computer_points < 2001:
        user_roll = user_roll_the_dice()
        user_points += user_roll
        print('user_points =', user_points)
        computer_roll = comp_roll_the_dice()
        computer_points += computer_roll
        print('computer_points =', computer_points)


if __name__ == '__main__':
    game()
