# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:34:44 2022

@author: Chema
"""

import random
import os

"""
In this exercise, we are going to implement a version of the popular Wordle but with numbers. 
So, the flow would be the next one:

1-Create a random number of 5 digits between 00000-99999. This is the target number to find out.

2-Create an initial number using random or making a permutation of the target number. 
Swap positions of that number to generate a new version containing the same digits but in different positions. 
This is a very simple strategy to make a permutations.

3-Configure a maximum number of attempts to find out the target number (3).

4-Start the game, showing the current number and asking the user to enter an attempt (only 5 digit numbers are allowed).

    Compare the user input with the target number and display the digits following the next strategy:
        -If the digit is in the target number and in the same position, the character will be displayed in Green or with some symbol (+).
        -If the digit is in the target number but not in the same position, the character will be displayer in Red or with some symbol (*).
        -If the digit is not in the target number, the character will be displayed in black (default console color) or with some symbol (-).

5-Technical approach:
    Make use of strings to manage the number positions and values.

"""

class Color:
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    RESET = '\033[0m'
    ORANGE ='\033[33m'


MIN = 10000
MAX = 99999

if __name__=="__main__":
    target_number = str(random.randint(MIN, MAX))
    SIZE = len(target_number)
    max_attempts = 5
    #Simple initial Permutation 
    #random.shuffle(current)
   
    #for pos in range(len(current)-1):
    #    current[pos], current[pos+1] = current[pos+1], current[pos]
    
    current = str(random.randint(MIN, MAX))
    #Only for debugging
    #print("[DEBUG] The target number is: "+target_number)
    
    #Program header
    print("______________________________________\n")    
    print("NUMBERL: a kind of Wordle for numbers")
    print("______________________________________\n")    
    print("A number with {} digits...".format(SIZE))
    print("{} attempts...".format(max_attempts))
    print(Color.GREEN +" correct digit and position.")
    print(Color.ORANGE +" correct digit but NOT position.")
    print(Color.RESET +" digit not in the number.")
    print("______________________________________\n")
    
    
  
    target = False
    n_attempts = 1
    
    while not target and n_attempts <= max_attempts:
        #Printing with colors
        for pos in range(len(target_number)):
            if target_number[pos] == current[pos]:
                print(Color.GREEN+current[pos]+" ", end="")
            elif current[pos] in target_number:
                print(Color.ORANGE+current[pos]+" ", end="")
            else:
                print(Color.RESET+current[pos]+" ", end="")
        print(Color.RESET)    
            
        #Validating input
        correct_input = False    
        while not correct_input:
            input_number = input("Attempt {} of {}-->".format(n_attempts, max_attempts))
            correct_input = len(input_number) == SIZE
            if not correct_input:
                print("Please enter a number with {} digits.".format(SIZE))
            
        #Checking if end
        target = input_number == target_number
        current =[x for x in input_number]
        n_attempts += 1    
    
    if target:
        print("Win in {} attempts!".format(n_attempts-1))        
    else:
        print("No more attempts, the number was: {}.".format(target_number))
    
    