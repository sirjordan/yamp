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
    :param n: 3 or 4
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


def score_straight(dices, sequence_count):
    """
    Four/Five sequential dice
    (1-2-3-4, 2-3-4-5, or 3-4-5-6) if 3 or (1-2-3-4-5 or 2-3-4-5-6) if 5 sequential
    :param sequence_count: 4 or 5 sequence
    :return: 30 if 4 sequential or 40 if 5 sequential
    """
    dices.sort()
    dice = dices[0]
    sequence = 1
    for seq in range(1, len(dices)):
        if dices[seq] == dice + 1:  # Next is +1 grater
            sequence += 1
        else:
            sequence = 1

        if sequence == sequence_count:
            break

        dice = dices[seq]

    if sequence == sequence_count:
        if sequence_count == 4:
            return 30
        elif sequence_count == 5:
            return 40
        else:
            raise ValueError('Parameter "n" must be 4 or 5 to count score')
    else:
        return 0


def score_yamp(dices):
    """
    All five dice the same
    :return: 50
    """
    for dice_num in range(MIN_DICE, MAX_DICE + 1):
        if count_equal(dices, dice_num) == DICE_COUNT:
            return 50

    return 0


def score_chance(dices):
    """
    Any combination
    :return: Sum of all dice
    """
    return sum(dices)























