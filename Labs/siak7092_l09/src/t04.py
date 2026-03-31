"""
-------------------------------------------------------
Validate Code
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-09"
-------------------------------------------------------
"""
# Imports
from functions import validate_code
# Constants
code = input("Enter a code: ")
cat, dig, qual = validate_code(code)

print(cat, dig, qual)
