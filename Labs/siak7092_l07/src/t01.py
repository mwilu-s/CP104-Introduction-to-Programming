"""
-------------------------------------------------------
Guess The Number Game
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-29"
-------------------------------------------------------
"""
# Imports
from functions import hi_lo_game
# Constants
high = int(input("Enter an upper bound number: "))
count = hi_lo_game(high)

print("You made {} guesses.".format(count))