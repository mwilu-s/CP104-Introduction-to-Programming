"""
-------------------------------------------------------
List Statistics
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-07"
-------------------------------------------------------
"""
# Imports
from functions import list_stats
# Constants
values = [94, 96, -22, -79, -28, -26, -50, 71, 24, -32]
smallest, largest, total, average = list_stats(values)
print(f"{smallest}, {largest}, {total}, {average}")
