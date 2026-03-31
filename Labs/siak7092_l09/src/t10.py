"""
-------------------------------------------------------
Text Analysis
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-09"
-------------------------------------------------------
"""
# Imports
from functions import text_analyze
# Constants
userText = input("Enter some text: ")
uppr, lowr, dgts,whtspc = text_analyze(userText)
print(uppr, lowr, dgts, whtspc)
