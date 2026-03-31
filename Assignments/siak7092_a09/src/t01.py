"""
-------------------------------------------------------
File Top
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-18"
-------------------------------------------------------
"""
# Imports
from functions import file_top
# Constants

num = int(input("Enter a number to stop at: "))
filename = "students.txt"
student_file = open(filename, "r", encoding="utf-8")
file_top(student_file, num)
student_file.close()