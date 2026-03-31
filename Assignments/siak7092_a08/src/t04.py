"""
-------------------------------------------------------
Validate ISBN
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-09"
-------------------------------------------------------
"""
# Imports
from functions import valid_isbn
# Constants
isbn = input("Enter isbn: ")
result = valid_isbn(isbn)
print(result)
