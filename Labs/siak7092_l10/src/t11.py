"""
-------------------------------------------------------
Find Longest Word
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-18"
-------------------------------------------------------
"""
# Imports
from functions import find_longest
# Constants

filename = "words.txt"
fh = open(filename, "r", encoding="utf-8")
word = find_longest(fh)
print(word)
fh.close()