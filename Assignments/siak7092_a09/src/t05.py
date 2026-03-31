"""
-------------------------------------------------------
Student Stats
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-18"
-------------------------------------------------------
"""
# Imports
from functions import student_stats
# Constants
filename = "students.txt"
fh = open(filename, "r", encoding="utf-8")
low_id, high_id, avg = student_stats(fh)
print(low_id, high_id, avg)
fh.close()
