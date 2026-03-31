"""
-------------------------------------------------------
Compound Interest
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-09-20"
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

principal = float(input("Principal: $"))
interest = float(input("Interest (%): "))
years = int(input("Number of years: "))
compounding = int(input("Number of times interest compounded per year: "))

amount = principal*(1+(interest/100)/12)**(years*compounding)


print("Balance: $", amount)