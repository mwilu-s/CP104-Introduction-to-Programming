"""
-------------------------------------------------------
Fahrenheit to Celsius
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# Imports
from functions import f_to_c
# Constants

fahrenheit = int(input("Enter the temperature in fahrenheit: "))
celsius = f_to_c(fahrenheit)
print(celsius)
