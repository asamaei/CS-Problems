"""
Author: Amir Samaei
Date: March 4, 2023
Description: This program contains solutions to practice problems for the CCPS 109 course at the University of Ryerson.
"""
def only_odd_digits(n):
    odd_digists = [1, 3, 5, 7, 9]
    current_state = False
    String_input = str(n)
    for i in range(len(String_input)):
     if int(String_input[i]) in odd_digists:
      current_state = True
     else:
        current_state = False
        break
    return current_state
