import random
dice = random.randint(1, 6)
special_dice = dice == 1 or dice == 6
print(f'you have rolled a {dice} and is it a special number: {special_dice}')