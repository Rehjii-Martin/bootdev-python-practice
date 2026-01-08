'''
Boot.dev – Learn to Code in Python
CH9: Lists
Problem: Slicing Lists

Description:
    Split a single list into 3 seperate lists based on parameters.
Notes:
    - 
Date: 2026-01-07
Source: Boot.dev Learn to Code in Python/Modulo Operator in Python
'''

# Problem

# Assignment
# Complete the given get_champion_slices function. It takes a list of champions and should return three new lists based on the given champions:

# First, return a slice of the champions list that starts with the third champion and goes to the end of the list.
# Next, return a slice of the champions list that starts at the beginning of the list and includes all champions except for the very last champion.
# Last, return a slice of the champions list that only includes the champions in even numbered indexes.

def get_champion_slices(champions):
    third = champions[2:]
    second = champions[:-1]
    first = champions[::2]

    return third, second, first