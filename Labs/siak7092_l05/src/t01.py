"""
-------------------------------------------------------
Magic Date
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-10"
-------------------------------------------------------
"""
# Imports
from functions import magic_date
# Constants
day = int(input("Enter a day: "))
month = int(input("Enter a month number: "))
year = int(input("Enter the last two digits of a year: "))

magic = magic_date(day,month,year)

print(f"{day},{month},{year} --> {magic}")
