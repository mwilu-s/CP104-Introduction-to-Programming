"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-29"
-------------------------------------------------------
"""
# Imports
from random import randint
# Constants
HIGHHOURS = 40
HHPERCENT = 1.5
TAX = 3.625/100
def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1,high)
    guess = int(input("Guess a number between 1 and {}: ".format(high)))
    count = 1;
    
    while guess != number:
        if guess < number:
            count = count + 1
            print("Too low, try again.")
            guess = int(input("Guess a number between 1 and {}: ".format(high)))
        else:
            count = count + 1
            print("Too high, try again.")
            guess = int(input("Guess a number between 1 and {}: ".format(high)))
    
    print("Congratulations - good guess!")
    return count



def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    num = 1
    
    while num < target:
        num = num * 2
    
    power = num
    return power




def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    square = 1
    final = 0
    
    while final <= target:
        final += square**2
        square = square + 1
    
    return final
    


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    
    exp = float(input("Enter an expense (0 to quit): "))
    expenses = 0
    balance = 0
    status = ""
    
    while exp != 0: 
        expenses = expenses + exp
        exp = float(input("Enter an expense (0 to quit): "))
    
    balance = available - expenses
    
    if balance < 0:
        status = "Deficit"
    elif balance > 0:
        status = "Surplus"
    else:
        status = "Balanced"
    
    return expenses, balance, status



def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    employeeID = int(input("Employee ID: "))
    total = 0
    count = 0
    while employeeID != 0:
        count = count + 1
        wph = int(input("Hourly wage rate: "))
        hours = int(input("Hourly wage rate: "))
        
        if hours > HIGHHOURS:
            remHours = hours - HIGHHOURS
            netWithoutTax = (wph * HIGHHOURS) + (remHours * wph * HHPERCENT)
            netWithTax = netWithoutTax - (netWithoutTax * TAX)
            total = total + netWithTax
            print(f"Net payment for employee {employeeID}: ${netWithTax:,.2f}")
        else:
            netWithoutTax = (wph * hours)
            netWithTax = netWithoutTax - (netWithoutTax * TAX)
            total = total + netWithTax
            print(f"Net payment for employee {employeeID}: ${netWithTax:,.2f}")
            
        employeeID = int(input("Employee ID: "))
    
    average = total/count
    return total, average
    