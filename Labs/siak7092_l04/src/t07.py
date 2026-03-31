"""
-------------------------------------------------------
Total Change
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# Imports
from functions import total_change
# Constants

nickel = int(input("Enter the number of nickels: "))
dime = int(input("Enter the number of dimes: "))
quarter = int(input("Enter the number of quarters: "))
loonie = int(input("Enter the number of loonies: "))
toonie = int(input("Enter the number of toonies: "))

total = total_change(nickel, dime, quarter, loonie, toonie)
print(f"{total:.2f}")
