"""
-------------------------------------------------------
Sorted Lists
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-07"
-------------------------------------------------------
"""
# Imports
from functions import verify_sorted
from functions import list_positives
# Constants

numbers = list_positives()
order, index = verify_sorted(numbers)

print(f"{order}, {index}")
