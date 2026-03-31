"""
-------------------------------------------------------
Budget
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-29"
-------------------------------------------------------
"""
# Imports
from functions import budget
# Constants

available = float(input("Enter amount available: $"))
exp, bal, stat = budget(available)
print(f"{exp:.2f}, {bal:.2f}, {stat}")
