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
    while user_points < 200 or computer_points < 200:
        user_roll = user_roll_the_dice()
        if user_roll == 7:
            user_points //= 7
        elif user_roll == 11:
            user_points *= 11
        else:
            user_points += user_roll
        print('user_points =', user_points)
        if user_points >= 200:
            print('You win!')
            break

        computer_roll = comp_roll_the_dice()
        if computer_roll == 7:
            computer_points //= 7
        elif computer_roll == 11:
            computer_points *= 11
        else:
            computer_points += computer_roll
        print('computer_points =', computer_points)
        if computer_points >= 200:
            print('I win!')
            break


if __name__ == '__main__':
    game()
