import random

MIN_DICE = 1
MAX_DICE = 6
DICE_COUNT = 5


def roll_dices():
    """
    Roll and return 5 randomly generated dices
    :return: [] of 5 ints
    """
    dices = []

    for i in range(DICE_COUNT):
        dice = random.randrange(MIN_DICE, MAX_DICE + 1)
        dices.append(dice)

    return dices


def count_equal(dices, num_to_match):
    count = 0
    for dice in dices:
        if dice == num_to_match:
            count += 1

    return count


def score_matching(dices, num_to_match):
    """
    Any combination
    :return: The sum of dice with the number 'num_to_match'
    """
    count = count_equal(dices, num_to_match)
    return count * num_to_match


def score_n_of_a_kind(dices, n):
    """
    At least three/four (n) dice the same
    :return: Sum of all dice
    """
    if n != 3 and n != 4:
        raise ValueError('Parameter "n" must be 3 or 4 to count score')

    for dice_num in range(MIN_DICE, MAX_DICE + 1):
        n_of_kind = count_equal(dices, dice_num)
        if n_of_kind >= n:
            return sum(dices)

    return 0


def score_full(dices):
    """
    Full = Three of one number and two of another
    :return: 25 if have Full
    """
    three_matched_num = 0
    for dice_num in range(MIN_DICE, MAX_DICE + 1):
        threes = count_equal(dices, dice_num) == 3
        if threes:
            three_matched_num = dice_num
            break

    two_matched_num = 0
    for dice_num in range(MIN_DICE, MAX_DICE + 1):
        if dice_num != three_matched_num:
            twos = count_equal(dices, dice_num)
            if twos == 2:
                two_matched_num = twos
                break

    if three_matched_num > 0 and two_matched_num > 0:
        return 25
    else:
        return 0

























