"""
-------------------------------------------------------
File Statistics
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-18"
-------------------------------------------------------
"""
# Imports
from functions import file_statistics
# Constants

filename = "addresses.txt"
fh = open(filename, "r", encoding="utf-8")
ucount, lcount, dcount, wcount, rcount = file_statistics(fh)
print(ucount, lcount, dcount, wcount, rcount)
fh.close()