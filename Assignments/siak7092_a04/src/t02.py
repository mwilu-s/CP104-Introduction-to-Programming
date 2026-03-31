"""
-------------------------------------------------------
Pollution Ranking
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-10"
-------------------------------------------------------
"""
# Imports
from functions import pollution_ranking
# Constants

airQuality = int(input("Enter an air quality index value: "))
pollution = pollution_ranking(airQuality)

print(pollution)

