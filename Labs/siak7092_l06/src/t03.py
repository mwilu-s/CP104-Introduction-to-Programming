"""
-------------------------------------------------------
Sum All
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-24"
-------------------------------------------------------
"""
# Imports
from functions import sum_all
# Constants

start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))
incr = int(input("Enter incrementing value: "))

total = sum_all(start,end,incr)

print(total)
