"""
-------------------------------------------------------
File Copy
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-18"
-------------------------------------------------------
"""
# Imports
from functions import file_copy
# Constants

filename1 = "words.txt"
filename2 = "new_words.txt"
fh_1 = open(filename1, "r", encoding="utf-8")
fh_2 = open(filename2, "w", encoding="utf-8")
file_copy(fh_1,fh_2)
fh_1.close()
fh_2.close()