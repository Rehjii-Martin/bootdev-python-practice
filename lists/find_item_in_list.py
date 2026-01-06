'''
Boot.dev – Python Track
CH9: Lists
Problem: Finding Items in a List

Description:
    Use no-index or no-range syntax to find items within list.

Notes:
    - [Repeated Error] double == for assignment, it is for boolean = is for assignment
    - for-loops do not need range nor index, looping and printing values is possible
Date: 2026-01-06
Source: Boot.dev Learn to Code in Python/Find an Item in a List
'''

# Problem
# Practice the "no-index" or "no-range" syntax:
    # for fruit in fruits:
    #     print(fruit)
# Assignment
# We need to check if a player has a specific item in their inventory. 
# In the contains_leather_scraps function, use the no-index syntax to iterate over each item in items. 
# If you find an item called Leather Scraps, set the found variable to True.

def contains_leather_scraps(items):
    found = False

    # don't touch above this line

    for item in items:
        if item == "Leather Scraps":
            found = True

    # don't touch below this line

    return found