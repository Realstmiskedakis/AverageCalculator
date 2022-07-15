"""
@Author: Stelios Miskedakis - @Realstmiskedakis / @Acidshell.gr
Language: Python '3.10.5'
Version: '1.0V'
About this program:

An average calculator can be used to calculate GPAs or anything else you need.

"""

# Packages / Libraries
import os

# The List
subjects_list = []


# The Average Function
def average_calculator():
    while True:
        try:
            os.system('cls')
            print(">> This is a average calculator, can be used to calculate GPAs or anything else you need.\n")
            user_subjects = int(input(">> Enter, how many subjects you want: "))
            for subjects in range(user_subjects):
                user_value = float(input(f">> {subjects} Enter a Value: "))
                subjects_list.append(user_value)
            os.system('cls')
            print(">> Your values is:", subjects_list, "now I'll calculate this list.\n")
            print(">> Results:", sum(subjects_list) / user_subjects)
            return None
        except(ValueError, TypeError, IndexError):
            print("Invalid Input, Exit.")
            break


average_calculator()
