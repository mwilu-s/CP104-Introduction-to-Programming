"""
-------------------------------------------------------
Falling Distance
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# Imports
from functions import falling_distance
# Constants
fallTime = int(input("Enter the time taken for the object to fall: "))
distance = falling_distance(fallTime)
print(distance)