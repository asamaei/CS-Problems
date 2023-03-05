"""
Author: Amir Samaei
Date: March 4, 2023
Description: This program contains solutions to practice problems for the CCPS 109 course at the University of Ryerson.
"""


def riffle(items, out=True):
  Lenght = len(items)
  first_half = items[0:Lenght//2]
  second_half = items[Lenght//2:]
  new_list = []

  if (out):
    for i in range(Lenght//2):
      new_list.append(first_half[i])
      new_list.append(second_half[i])
  else:
    for i in range(Lenght//2):
      new_list.append(second_half[i])
      new_list.append(first_half[i])
  return new_list