"""
-------------------------------------------------------
Customer Record
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-18"
-------------------------------------------------------
"""
# Imports
from functions import customer_record
# Constants

num = int(input("Enter a number to search for: "))
filename = "customers.txt"
customer_file = open(filename, "r", encoding="utf-8")
result = customer_record(customer_file, num)
print(result)
customer_file.close()