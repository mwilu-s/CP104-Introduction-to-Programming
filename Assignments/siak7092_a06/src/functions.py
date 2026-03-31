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

# Constants
GOLD = "gold"
PURPLE = "purple"
DIV = 10

def total_wins():
    """
    -------------------------------------------------------
    Asks the user to input the winning team of each round 
    and stops when the user enters nothing (presses enter 
    or return). It then counts how many times the purple
    and gold teams won.
    
    Use: purple, gold = total_wins() 
    -------------------------------------------------------
    Parameters:
        none
    Returns:
        purple - The number of times the user has entered the purple team (int)
        gold - The number of times the user has entered the gold team (int)
    ------------------------------------------------------
    """
    purple = 0
    gold = 0
    team = input("Enter the winning team: ")
    
    while team != '':
        if team.lower() == GOLD:
            gold = gold + 1
            team = input("Enter the winning team: ")
            
        elif team.lower() == PURPLE:
            purple = purple + 1
            team = input("Enter the winning team: ")
        
        else:
            team = input("Enter the winning team: ")
            
    
    return purple, gold



def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    num = 1
    prime = True
    
    while num <= number and prime == True:
        if number % num == 0 and num != 1 and num != number:
            prime = False
        else:
            num = num + 1
    
    return prime
            

def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"Principal: ${principal_amount:.2f}")
    print(f"Interest Rate: {interest_rate:.2f}%")
    print(f"Monthly Payment: ${payment:.2f}")
    print("----------------------------------")
    print("Month\tInterest\tPayment\tBalance")
    print("----------------------------------")

    month = 1
    interest1 = interest_rate/100
    
    while principal_amount > 0:
        interest2 = (principal_amount * interest1)/12
        principal_amount = (principal_amount + interest2) - payment
        
        if principal_amount < 0:
            payment = payment + principal_amount
            principal_amount = 0
            
            
        print(f"{month:6d}{interest2:>12.2f}{payment:>12.2f}{principal_amount:>12.2f}")
        month = month + 1
    
    return None


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    digits = 0
    if number == 0:
        digits = 1
    elif number > 0:
        while number > 1:
            number = number/10
            digits = digits + 1
    
    else:
        while number < -1:
            number = number/10
            digits = digits + 1
    
    return digits


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    factor = 1
    total = 0
    while factor < number:
        if number % factor == 0:
            total = total + factor
        
        factor = factor + 1
    
    return total
            
    
        
        
    
    

            