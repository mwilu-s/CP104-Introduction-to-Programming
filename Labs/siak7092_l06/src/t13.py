"""
-------------------------------------------------------
Lumber
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-24"
-------------------------------------------------------
"""
# Imports
from functions import lumber
# Constants

baseMin = int(input("Enter base minimum: "))
baseMax = int(input("Enter base maximum: "))
baseInc = int(input("Enter base increment: "))
heightMin = int(input("Enter height minimum: "))
heightMax = int(input("Enter height maximum: "))
heightInc = int(input("Enter height increment: "))

lumber(baseMin, baseMax, baseInc, heightMin, heightMax, heightInc)

