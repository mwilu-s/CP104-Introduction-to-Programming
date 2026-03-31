"""
-------------------------------------------------------
Wind Speed
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-10"
-------------------------------------------------------
"""
# Imports
from functions import wind_speed
# Constants

speed = int(input("Enter the wind speed (km/h): "))

results = wind_speed(speed)

print(results)