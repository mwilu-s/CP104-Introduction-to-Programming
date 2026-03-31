"""
-------------------------------------------------------
Calories Burned On A Treadmill
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-25"
-------------------------------------------------------
"""
# Imports
from functions import calories_treadmill
# Constants

calories = float(input("Enter the amount of calories burned per minute: "))
mins = int(input("Enter the number of minutes on the treadmill: "))
calories_treadmill(calories,mins)
