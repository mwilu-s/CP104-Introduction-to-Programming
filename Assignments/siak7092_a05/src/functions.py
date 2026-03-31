"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-25"
-------------------------------------------------------
"""
# Imports

# Constants
INC = 5
CHAR = "#"



def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1
    
    for i in range(number,0,-1):
        product *= i
    
    return product


def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Calculates the number of calories burned
    every five minutes and prints a table
    Use: calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - calories burned per minute (float > 0)
        minutes - number of minutes spent on the treadmill (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(INC, minutes + 1, INC):
        calories = per_min * i
        print(f"{i:2d}{calories:5.1f}")
    
    return None

def arrow_up(rows):
    """
    -------------------------------------------------------
    Prints an upwards arrow of rows of characters using
    the char character.
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the arrow (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(rows):
        for j in range((2*rows) - 1):
            if i + j == rows - 1 or j - i == rows - 1:
                print(CHAR, end = '')
            else:
                print(' ', end = '')    
        print()
        
    return None
    
    
def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for i in range(start_num,stop_num + 1):
        print(f"{i}|", end = '')
        for j in range(start_num, stop_num + 1):
            product = i * j
            print(f"{product:4d}", end = '')
        print()
    
    return None

def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    
    total = 0
    
    for i in range(start,(count)*increment,increment):
        total += i
    
    return total