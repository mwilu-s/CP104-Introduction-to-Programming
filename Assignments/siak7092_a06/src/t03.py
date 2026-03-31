"""
-------------------------------------------------------
Interest Table
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-29"
-------------------------------------------------------
"""
# Imports
from functions import interest_table
# Constants
amount = float(input("Enter the principal amount: $"))
interest = float(input("Enter the interest rate (%): "))
payments = float(input("Enter payment amount: $"))
interest_table(amount,interest,payments)

