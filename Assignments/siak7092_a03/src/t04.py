"""
-------------------------------------------------------
Products of Fractions
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# Imports
from functions import multiply_fractions
# Constants
num1 = int(input("Enter the first numerator: "))
den1 = int(input("Enter the first denominator: "))
num2 = int(input("Enter the second numerator: "))
den2 = int(input("Enter the second denominator: "))

numerator, denominator, product = multiply_fractions(num1, den1, num2, den2)
print(f"{numerator}, {denominator}, {product}")
