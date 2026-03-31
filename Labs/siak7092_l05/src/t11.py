"""
-------------------------------------------------------
Plane Coordination
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-10"
-------------------------------------------------------
"""
# Imports
from functions import quadrant
# Constants

x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

location = quadrant(x,y)

print(location)
