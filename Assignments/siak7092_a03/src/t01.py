"""
-------------------------------------------------------
Square Feet to Acres
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# Imports
from functions import footage_to_acres
# Constants

feet = float(input("Enter the square feet: "))
acres = footage_to_acres(feet)
print(acres)