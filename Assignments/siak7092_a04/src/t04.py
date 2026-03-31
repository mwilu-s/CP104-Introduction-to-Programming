"""
-------------------------------------------------------
Colour Combine
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-10"
-------------------------------------------------------
"""
# Imports
from functions import colour_combine
# Constants

colour1 = input("Enter one of red, green or blue: ")
colour2 = input("Enter one of red, green or blue: ")

colour = colour_combine(colour1, colour2)

print(colour)
