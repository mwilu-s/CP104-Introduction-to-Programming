"""
-------------------------------------------------------
Line Numbering
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-18"
-------------------------------------------------------
"""
# Imports
from functions import line_numbering
# Constants

filename1 = "wilde.txt"
filename2 = "wilde_numbered.txt"
fh_1 = open(filename1, "r", encoding="utf-8")
fh_2 = open(filename2, "w", encoding="utf-8")
line_numbering(fh_1, fh_2)
fh_1.close()
fh_2.close()