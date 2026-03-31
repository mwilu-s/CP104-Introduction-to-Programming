"""
-------------------------------------------------------
Mowing
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# Imports
from functions import lawn_mow_time
# Constants

wide = float(input("Enter the width of the lawn: "))
length = float(input("Enter the length of the lawn: "))
speed = float(input("Enter the speed: "))

time = lawn_mow_time(wide, length, speed)
print(time)