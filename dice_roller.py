#!/usr/bin/python3

# Name: Derick Demers
# Date: March 22th 2026
# Program name: dice_roller.py
# This program The purpose of this program is to roll the dice based on the number of dice and the number of die faces inputted by the user. 
 
#variable
number_dice = 0
number_side = 0
u_input = ""

#import the library radom
import random

#welcom message
print(f"///Welcome\\\\\\\\")

#promt user for specification
number_dice = int(input("How many dice would you like to be thrown: "))
while number_dice == 0:
    number_dice = int(input("Dice thrown cannot be 0, how many should be trown?: "))

number_side = int(input("Enter how many side the dice will have: "))
while number_side == 0:
    number_side = int(input("A dice can not have 0 sides, how many should it?: "))

# Calculate min and max values
min_value = number_dice * 1
max_value = number_dice * number_side

# Roll the dice
while u_input != "q":
    result = random.randint(min_value, max_value)
    
    # Check for maximum value
    if result == max_value:
        print(f"You rolled: {result}. Congratulations! That is the maximum value!")
    else:
        # Display the result
        print(f"You rolled: {result}")
        u_input = input("Press Enter to roll agian (or 'q' to quit): ")

print("GoodBye!")