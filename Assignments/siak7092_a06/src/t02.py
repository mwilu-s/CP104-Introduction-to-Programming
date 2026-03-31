"""
-------------------------------------------------------
Detect Prime Number
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-29"
-------------------------------------------------------
"""
# Imports
from functions import detect_prime
# Constants

num = int(input("Enter a number greater than 1: "))
prime = detect_prime(num)

print(prime)