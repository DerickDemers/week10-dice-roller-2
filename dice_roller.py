#!/usr/bin/python3

# Name: Derick Demers
# Date: March 22th 2026
# Program name: dice_roller.py
# This program The purpose of this program is to roll the dice based on the number of dice and the number of die faces inputted by the user. 
 
#import the library radom
import random

#welcom message
print(f"///Welcome\\\\\\\\")

#promt user for specification
number_dice = int(input("Enter how many dice will be thrown: "))
number_side = int(input("Enter how many side the dice will have: "))

# Calculate min and max values
min_value = number_dice * 1
max_value = number_dice * number_side

# Roll the dice

result = random.randint(min_value, max_value)

# Display the result
print(f"You rolled: {result}")

# Check for maximum value
if result == max_value:
    print("Congratulations! You rolled the maximum value!")