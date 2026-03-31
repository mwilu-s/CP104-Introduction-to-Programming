"""
-------------------------------------------------------
Mortgage Payment
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
    
mortgage = float(input("Enter the mortgage principal ($): "))
yearlyInterest = float(input("Enter the yearly interest rate (%): "))
years = int(input("Enter the number of years the mortgage is to run: "))
months = years * 12
monthlyRate = (yearlyInterest/100)/12

monthlyPayments = mortgage * ( (monthlyRate*(1 + monthlyRate)**months) / ((1 + monthlyRate)**months - 1))

print("The monthly payments are : $", monthlyPayments)
