#!/usr/bin/env python3
# diceroll.py
import random
import sys

def parse_input(input_string):
    """Parse 'input_string' and return it as a list"""

    # Checks to see if user input an 'end' command. If yes, exits program.

    if input_string == 'e': 
        sys.exit()

    input_split = input_string.strip()
    input_split = input_string.split("d", 1)
    
    return input_split

def roll_dice(dice):
    """return the value of 'dice_num' rolls of 'dice_sides' dice"""

    try:
        dice_num = int(dice[0])
        dice_sides = int(dice[1])
    except (ValueError, IndexError):
        print("Invalid Input")
        return []

    # Roll the dice
    roll_results = []
    for _ in range(dice_num):
        roll = random.randint(1, dice_sides)
        roll_results.append(roll)
    
    return roll_results

# Main code block
print ("Welcome to dice roller. Input dice to roll in the format (x)d(y). To end, input 'e'.\n")

while True:
    dice_input = input(">> ")
    dice = roll_dice(parse_input(dice_input))
    if len(dice) != 0:
        print(f'Total: {sum(dice)}, Rolls: {dice}')
