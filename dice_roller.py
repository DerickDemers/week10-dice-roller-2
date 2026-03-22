#!/usr/bin/python3

# Name: Derick Demers
# Date: March 22th 2026
# Program name: dice_roller.py
# This program The purpose of this program is to roll the dice based on the number of dice and the number of die faces inputted by the user. 

#import the library radom
import random

def get_numdice():
    #Get the number of die faces. 
    number_dice = int(input("How many dice would you like to be thrown: "))
    while number_dice == 0:
        number_dice = int(input("Dice thrown cannot be 0, how many should be trown?: "))
    return number_dice

def get_diefaces():
    #Get the number of dice. 
    number_side = int(input("Enter how many side the dice will have: "))
    while number_side == 0:
        number_side = int(input("A dice can not have 0 sides, how many should it?: "))
    return number_side

def is_max_score(result,max_value):
    if result == max_value:
        return True
    else:
        return False

def roll_dice(number_dice,number_side):
    # Calculate min and max values
    min_value = number_dice * 1
    max_value = number_dice * number_side

    # Roll the dice
    u_input = ""
    while u_input != "q":
        result = random.randint(min_value, max_value)
    
        
        if is_max_score(result,max_value) == True:
            #Display a congratulatory message when the roll is equal to the maximum value that can be rolled. 
            print(f"You rolled: {result}. Congratulations! That is the maximum value!")
        else:
            # Display the result
            print(f"You rolled: {result}")
        
        #Prompt for another round. 
        u_input = input("Press Enter to roll agian (or 'q' to quit): ")

#welcom message
print(f"///Welcome\\\\\\\\")

#Get the number of die faces. 
number_dice = get_numdice()

#Get the number of dice. 
number_side = get_diefaces()

#Roll the dice. 
result = roll_dice(number_dice,number_side)

print("GoodBye!")