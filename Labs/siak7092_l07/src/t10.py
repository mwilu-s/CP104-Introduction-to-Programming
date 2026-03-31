"""
-------------------------------------------------------
Employee Payroll
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-29"
-------------------------------------------------------
"""
# Imports
from functions import employee_payroll
# Constants

total, average = employee_payroll()

print(f"{total:,.2f}, {average:,.2f}")