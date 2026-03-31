"""
-------------------------------------------------------
Fahrenheit to Celsius
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-09-19"
-------------------------------------------------------
"""
# Imports

# Constants

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """
    
    
fahrenheit = int(input("Enter the temperature in degrees Fahrenheit: "))
FREEZE = 32
celsius = (fahrenheit - FREEZE) * (5/9)
    
print("Temperature (C): ", celsius)