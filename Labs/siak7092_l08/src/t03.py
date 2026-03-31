"""
-------------------------------------------------------
Digit Names
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-07"
-------------------------------------------------------
"""
# Imports
from functions import get_digit_name
# Constants

userDigit = int(input("Enter a digit: "))
name = get_digit_name(userDigit)
print(name)