
"""
Author: Amir Samaei
Date: March 4, 2023
Description: This program contains solutions to practice problems for the CCPS 109 course at the University of Ryerson.
"""


def is_ascending(items):
    if len(items) < 2:  # Check if the length of the sequence is less than 2
        return True  # If the sequence is empty or has only one element, it is always ascending

    for i in range(1, len(items)):  # Iterate through the sequence starting from the second element
        if items[i] <= items[i - 1]:  # Check if the current element is less than or equal to the previous element
            return False  # If any adjacent pair of elements violates the ascending order, return False

    return True  # If all adjacent pairs of elements satisfy the ascending order, return True

