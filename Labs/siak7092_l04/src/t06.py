"""
-------------------------------------------------------
Pythag
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# Imports
from functions import pythag
# Constants
s1 = float(input("Enter side 1: "))
s2 = float(input("Enter side 2: "))
radius, diameter, circum, area = pythag(s1,s2) 
print(f"{radius}, {diameter}, {circum}, {area}")