from roll_the_dice import roll_the_dice
import random


def user_roll_the_dice():
    '''
    Function simulates rolling two dice which choose the player.
    :return: the amount of rolls, type - int
    '''
    text = 'Choose a dice from the set: D3, D4, D6, D8, D10, D12, D20, D100.'
    while True:
        try:
            roll_twice = [roll_the_dice(input(text).upper()), roll_the_dice(input(text).upper())]
            return sum(roll_twice)
        except Exception:
            print('not valid')


def computer_roll_the_dice():
    '''
    Function simulates rolling two random dice.
    :return: the amount of rolls, type - int
    '''
    cube_types = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    rand_choice = random.choice(cube_types)
    roll_twice = [roll_the_dice(rand_choice), roll_the_dice(rand_choice)]
    return sum(roll_twice)


def user_round(points):
    '''
    Function checks the sum of the rolls.
    :return: score result, type - int
    '''
    new_points = points
    rolling = user_roll_the_dice()
    if rolling == 7:
        new_points //= 7
    elif rolling == 11:
        new_points *= 11
    else:
        new_points += rolling
    return new_points


def computer_round(points):
    '''
    Function checks the sum of the rolls.
    :return: score result, type - int
    '''
    new_points = points
    rolling = computer_roll_the_dice()
    if rolling == 7:
        new_points //= 7
    elif rolling == 11:
        new_points *= 11
    else:
        new_points += rolling
    return new_points


def game():
    '''
    Function, checks the results of the players' points, if the result
    is equal to or greater than 2001 - the game is finished, the player has won.
    :user_points type: int
    :computer_points type: int
    '''
    user_points = 0
    computer_points = 0
    while user_points < 2001 or computer_points < 2001:
        print('Press ENTER to roll the dice')
        input()
        user_points = user_round(user_points)
        print('user points =', user_points)

        computer_points = computer_round(computer_points)
        print('compute points =', computer_points)

        if user_points >= 2001:
            print('You win!')
            break
        elif computer_points >= 2001:
            print('I win!')
            break


if __name__ == '__main__':
    game()
