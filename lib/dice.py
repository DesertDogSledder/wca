import random
import re


def roll(dice_string):
    # Calculates a dice roll in the format '1d6+2' or similar
    dice_rolled = []
    output = dict()
    match = re.search('(\d)d(\d)(.*)', dice_string)
    if match is not None:
        num_dice = int(match.group(1))
        num_sides = int(match.group(2))

        if match.group(3) == '':
            modifier = 0
        else:
            modifier = eval(match.group(3))

        for i in range(0, num_dice):
            dice_rolled.append(random.randint(1, num_sides))

        output['dice_rolled'] = dice_rolled
        output['modifier'] = modifier
        output['total'] = sum(dice_rolled) + modifier
    else:
        output['dice_rolled'] = 0
        output['modifier'] = 0
        output['total'] = int(dice_string)

    return output
