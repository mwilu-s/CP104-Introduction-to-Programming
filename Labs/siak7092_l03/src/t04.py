"""
-------------------------------------------------------
Discount
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
    
userNumber = float(input("Enter number: "))
percent = float(input("Enter percent: "))

discount = userNumber*(percent/100)
print(f"A {percent:.1f} percent discount on {userNumber:.1f} is {discount:.1f}")