"""
-------------------------------------------------------
Find Position
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-20"
-------------------------------------------------------
"""
# Imports
from functions import find_position
# Constants

matrix = [[3,9,-1],[2,34,7]]
small, large = find_position(matrix)
print(small, large)