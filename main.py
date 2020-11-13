import random


def roll_the_dice():
    '''
    Function simulates rolling two six-sided dice.
    :return: the amount of rolls, type - int
    '''
    roll_twice = [random.randint(1, 6), random.randint(1, 6)]
    return sum(roll_twice)


def game_rounds(points):
    '''
    Function checks the sum of the rolls: if the sum = 7, the points are divided
    without a remainder by 7, if the sum = 11 - the points are multiplied by 11,
    if the sum is any other number - the sum is added to the points.
    :return: score result, type - int
    '''
    new_points = points
    rolling = roll_the_dice()
    if rolling == 7:
        new_points //= 7
    elif rolling == 11:
        new_points *= 11
    else:
        new_points += rolling
    return new_points


def game():
    '''
    The main function, checks the results of the players' points, if the result
    is equal to or greater than 2001 - the game is finished, the player has won.
    :user_points type: int
    :computer_points type: int
    '''
    user_points = 0
    computer_points = 0
    while user_points < 2001 or computer_points < 2001:
        print('Press ENTER to roll the dice')
        input()
        user_points = game_rounds(user_points)
        print('user points =', user_points)

        computer_points = game_rounds(computer_points)
        print('compute points =', computer_points)

        if user_points >= 2001:
            print('You win!')
            break
        elif computer_points >= 2001:
            print('I win!')
            break


if __name__ == '__main__':
    game()
