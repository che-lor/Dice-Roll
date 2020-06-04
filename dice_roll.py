#!/usr/bin/env python3

import random #prints random from min,max
import time #sleeps in between commands

roll_again = "y"
min = 1
max = 6

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    time.sleep(1)
    print("The values are...")
    time.sleep(2)
    dice1 = random.randint(min, max)
    dice2 = random.randint(min, max)
    diceTotal = dice1 + dice2
    print(dice1, "and", dice2)
    time.sleep(1)
    print ("Dice total is", diceTotal)
    time.sleep(2)
    roll_again = input("Roll the dices again? [y/n] ")
    time.sleep(.5)

while roll_again == "no" or roll_again == "n":
	print("Okay, goodbye!")
	time.sleep(.5)
	break