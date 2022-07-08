"""
@Author: Stelios Miskedakis - @Realstmiskedakis / @Acidshell.gr
Language: Python '3.10.5'
Version: '1.0V'
About this program:

An average calculator can be used to calculate GPAs or anything else you need


"""

# Packages / Libraries
import os


# The Average Calculation Function
def average():
    while True:
        try:
            os.system('cls')
            # It's a function that calculates the average of the user's input.
            average_confirm = []
            user = int(input(">> How many subjects you want?: "))
            for i in range(user):
                user_value = float(input(f"{i} Enter a value: "))
                average_confirm.append(user_value)
            print("Is it Correct?:", average_confirm)
            user_confirm = input("Answer w/ ( Yes / No ): ").lower()
            if user_confirm in ['yes', 'y']:
                print(">> Your Average Results is: ", sum(average_confirm) / user)
            else:
                print(">> Rerun the program.")
            break
        except(TypeError, ValueError, InterruptedError):
            print("Invalid Input, Exit.")
            break


average()
