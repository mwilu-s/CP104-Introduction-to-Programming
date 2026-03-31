"""
-------------------------------------------------------
Divisibility
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-10"
-------------------------------------------------------
"""
# Imports
from functions import is_divisible
# Constants

num1 = int(input("Enter a whole number: "))
div1 = int(input("Enter a whole number: "))
div2 = int(input("Enter a whole number: "))

results = is_divisible(num1, div1, div2)

print(f"{num1}, {div1}, {div2} --> {results}")
