"""
-------------------------------------------------------
Read Integers
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-18"
-------------------------------------------------------
"""
# Imports
from functions import read_integers
# Constants

filename = "numbers.txt"
fh = open(filename, "r", encoding="utf-8")
numList = read_integers(fh)
print(numList)
fh.close()