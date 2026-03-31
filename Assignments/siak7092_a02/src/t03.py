"""
-------------------------------------------------------
Date Extraction
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
    
date = int(input("Enter a date in the format YYYYMMDD: "))
year = date // 10000
month = (date//100) - (year *100)
day = date - (year*10000) - (month * 100)

print(f"The reformatted date: {year:0d}/{month:02d}/{day:02d}")