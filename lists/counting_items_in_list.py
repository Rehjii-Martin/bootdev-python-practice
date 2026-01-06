# Problem

# Our players need a way to see how many copies of a specific item they have within their inventory!
# Let's finish the get_item_counts function.
# Within the loop, check if the items are a Potion, Bread, or Shortsword.
# If you find a match, increment the corresponding counter, either potion_count, bread_count or shortsword_count. """


'''
Boot.dev – Python Track
CH9: Lists
Problem: Counting Items in a List

Description:
    Use a loop to count items in a list by enumerating a counter based on the
    presence of an item within the list.

Notes:
    - if statements do not need else-blocks at all, they can terminate on completion
    - returning is not necessary within loop

Date: 2026-01-06
Source: Boot.dev Learn to Code in Python/Counting Items in a List
'''

def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

        for i in range(0, len(items)):
            if items[i] == "Potion":
                potion_count += 1
            if items[i] == "Bread":
                bread_count += 1
            if items[i] == "Shortsword":
                shortsword_count += 1

    # don't touch below this line

    return potion_count, bread_count, shortsword_count
