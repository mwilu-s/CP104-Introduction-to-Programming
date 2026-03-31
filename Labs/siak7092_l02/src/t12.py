"""
-------------------------------------------------------
Seconds Conversion
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-09-19"
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
    
userSeconds = int(input("Enter an amount of seconds: "))
SPM = 60

days = (userSeconds // (SPM**2 * 24)) % 24
hours = (userSeconds // SPM**2) % 24
minutes = (userSeconds // SPM) % SPM
seconds = userSeconds % SPM

print("days: ", days, "hours: ", hours, "minutes: ", minutes, "seconds: ", seconds)