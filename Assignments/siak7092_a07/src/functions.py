"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-07"
-------------------------------------------------------
"""
# Imports

# Constants

def list_factors(number):
    """
    -------------------------------------------------------
    Gets a whole numbers from a user and returns all of 
    its factors in a list.
    Use: factors = list_factors(number)
    -------------------------------------------------------
    Parameters:
        number - any whole number (int )
    Returns:
        factors - A list of factors of the number (list of int)
    ------------------------------------------------------
    """
    
    factors = []
    
    for i in range(1, number, 1):
        if number % i == 0:
            factors.append(i)
    
    
    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    number_list = []
    num = int(input("Enter a positive number: "))
    while num != 0:
        if num > 0:
            number_list.append(num)
            num = int(input("Enter a positive number: "))
        else:
            num = int(input("Enter a positive number: "))
    
    return number_list


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index = 0
    index_list = []
    
    for i in numbers:
        if i == target_number:
            index_list.append(index)
            index = index + 1
        else:
            index+1
    
    return index_list

def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for i in subtrahend:
        while i in minuend:
            minuend.remove(i)

    return None


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    index = -1
    in_order = True 
    len1 = len(numbers)
    
    for i in range(len1 - 1):
        if numbers[i] > numbers[i + 1]:
            index = i
            in_order = False 
    
    return in_order, index
        
    
    
            
            
        
            
    
        
        
        