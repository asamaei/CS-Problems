
"""
Author: Amir Samaei
Date: March 4, 2023
Description: This program contains solutions to practice problems for the CCPS 109 course at the University of Ryerson.
"""

def is_ascending(items):
 if len(items) < 2: # return True  # An empty sequence or a sequence with one element is always ascending
    return True
 for i in range(1, len(items)):
     if items[i] <= items[i - 1]:#return False  # The sequence is not strictly ascending if any adjacent pair of elements violates the condition
 return True  # All adjacent pairs of elements satisfy the condition, so the sequence is strictly ascending
