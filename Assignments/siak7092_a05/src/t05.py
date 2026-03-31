"""
-------------------------------------------------------
Range Addition
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-25"
-------------------------------------------------------
"""
# Imports
from functions import range_addition
# Constants
start = int(input("Enter starting number: "))
inc = int(input("Enter incrementing number: "))
count = int(input("Enter counting number: "))

total = range_addition(start,inc,count)

print(total)