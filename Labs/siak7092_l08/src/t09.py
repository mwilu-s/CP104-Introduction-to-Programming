"""
-------------------------------------------------------
Many Searches
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-07"
-------------------------------------------------------
"""
# Imports
from functions import many_search
# Constants
n = int(input("Enter the amount of numbers you want to enter: "))
values = []
for i in range(n):
    num = float(input("Enter number: "))
    values.append(num)

value = float(input("Enter number to search for: "))

indexes = many_search(values, value)

print(indexes)
    
