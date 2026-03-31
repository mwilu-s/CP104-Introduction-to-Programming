"""
-------------------------------------------------------
Date Reformatter
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# Imports
from functions import extract_date
# Constants

date = int(input("Enter a date in the format YYYYMMDD: "))
year,month,day = extract_date(date)
print(f"{year:0d}, {month:02d}, {day:02d}")
