"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-09-27"
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
    
flyers = int(input("Number of flyers: "))
deliveryPeople = int(input("Number of delivery people: "))

flyerPP = flyers//deliveryPeople
rem = flyers % deliveryPeople

print("Flyers per delivery person: ", flyerPP)
print("Flyers left over: ", rem)