'''
Boot.dev – Learn to Code in Python
CH9: Lists
Problem: Finding the Remainder

Description:
    Use modulo operator to check if numbers are odd, append to list if so.
Notes:
    - 
Date: 2026-01-07
Source: Boot.dev Learn to Code in Python/Modulo Operator in Python
'''


def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        if i % 2 != 0:
            odd_numbers.append(i)

    # don't touch below this line

    return odd_numbers