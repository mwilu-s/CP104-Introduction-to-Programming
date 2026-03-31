"""
-------------------------------------------------------
Parse Code
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-09"
-------------------------------------------------------
"""
# Imports
from functions import parse_code
# Constants

code = input("Enter a code: ")
pc, pi, pa = parse_code(code)

print(pc + "," + pi + "," + pa)
