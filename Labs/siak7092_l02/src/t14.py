"""
-------------------------------------------------------
Mac and Cheese Recipe
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-09-19"
-------------------------------------------------------
"""
# Imports

# Constants

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """

servings = int(input("Enter servings of Mac & Cheese: "))
MILK = 4
BUTTER = 8
FLOUR = 0.5
SALT = 2

servingsCalc = servings/6

milk = MILK * servingsCalc
butter = BUTTER * servingsCalc
flour = FLOUR * servingsCalc
salt = SALT * servingsCalc

print(servings, " servings of Mac & Cheese requires: \nmilk (cups): ", milk, "\nbutter (tablespoons): ", butter, "\nflour (cups): ", flour, "\nsalt (teaspoons): ", salt)

