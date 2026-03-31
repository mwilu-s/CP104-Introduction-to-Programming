"""
-------------------------------------------------------
Digits
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-09-27"
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
    
number = int(input("Enter a positive digit number: "))
num1 = number//10
num2 = number - (num1*10)
difference = num1 - num2

print("The difference of the digits of",number, "is", difference)