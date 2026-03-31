"""
-------------------------------------------------------
Count Frequency Word
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-18"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency_word
# Constants
word = input("Word to count: ")
filename = "words.txt"
fh = open(filename, "r", encoding="utf-8")
count = count_frequency_word(fh, word)
print(count)
fh.close()