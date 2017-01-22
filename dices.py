import random

DICE_COUNT = 5


def roll_dices():
    """
    Roll and return 5 randomly generated dices
    :return: [] of 5 ints
    """
    min_num = 1
    max_num = 6
    dices = []

    for i in range(DICE_COUNT):
        dice = random.randrange(min_num, max_num + 1)
        dices.append(dice)

    return dices


def score_matching(dices, num_to_match):
    """
    Any combination
    :return: The sum of dice with the number 'num_to_match'
    """
    count = 0
    for d in dices:
        if d == num_to_match:
            count += num_to_match

    return count


def score_n_of_a_kind(dices, n):
    """
    At least three/four (n) dice the same
    :return: Sum of all dice
    """
    if n != 3 and n != 4:
        raise ValueError('Parameter "n" must be 3 or 4 to count score')

    for dice_num in range(DICE_COUNT):
        n_of_count_num = 0
        for d in dices:
            if d == dice_num + 1:
                n_of_count_num += 1
        if n_of_count_num >= n:
            return sum(dices)

    return 0






