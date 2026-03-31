"""
-------------------------------------------------------
Annual Tax
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
    
TAX = 18.5
totalSales = int(input("Enter the total sales: $"))
salesTax = totalSales * (TAX/100)

print(f"""Projected Tax Report
--------------------------
{'Total Sales:':15s} $ {totalSales:,.2f}
{'Annual Tax:':15s} % {TAX:.2f}
--------------------------
{'Tax':15s} $ {salesTax:,.2f}
""")