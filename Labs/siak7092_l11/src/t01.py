"""
-------------------------------------------------------
Generate Matrix Num
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-20"
-------------------------------------------------------
"""
# Imports
from functions import generate_matrix_num
# Constants

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
low = int(input("Enter a lower bound: "))
high = int(input("Enter an upper bound: "))
valueType = input("Choose a type, 'float' or 'int': ")
matrix = generate_matrix_num(rows, cols, low, high, valueType)
print(matrix)