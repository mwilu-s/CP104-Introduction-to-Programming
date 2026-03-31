"""
-------------------------------------------------------
Number Stats
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-18"
-------------------------------------------------------
"""
# Imports
from functions import number_stats
# Constants

filename = "numbers.txt"
fh = open(filename, "r", encoding="utf-8")
smallest, largest, total, average = number_stats(fh)
print(f"{smallest}, {largest}, {total}, {average:.2f}")
fh.close()
