"""
-------------------------------------------------------
Slope
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# Imports
from functions import slope
# Constants
x1 = float(input("Enter the first x value: "))
y1 = float(input("Enter the first y value: "))
x2 = float(input("Enter the second x value: "))
y2 = float(input("Enter the second y value: "))
slp = slope(x1,y1,x2,y2)
print(slp)
