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

def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """
    digitNames = ["zero", "one", "two", "three","four","five","six","seven","eight","nine"]
    
    name = digitNames[n]
    
    return name



def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    total = 0
    smallest = values[0]
    largest = values[0]
    
    for i in values:
        if smallest > i:
            smallest = i
        
        if largest < i:
            largest = i
        
        total = total + i
        
    average = total/len(values)
    
    return smallest,largest,total,average


def many_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        indexes - a list of indexes of the location of value in values,
            [] if not found (list of int).
    -------------------------------------------------------
    """
    num = 0
    indexes = []
    for i in values:
        if i == value:
            indexes.append(num)
            num = num + 1
        else:
            num = num+1
    
    return indexes


def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sums(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    i = 0
    num = len(source1)
    target = []
    
    for i in range(num):
        s1 = source1[i]
        s2 = source2[i]
        total = s1 + s2
        target.append(total)
    
    return target


def intersection(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the intersection of the contents of source1 and source2.
    Only elements that appear in both source1 and source2
    appear once and only once in target.
    Use: target = intersection(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the intersection of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    i = 0
    len1 = len(source1)
    len2 = len(source2)
    target = []
    
    for i in range(len1):
        for j in range(len2):
            if len(target) == 0:
                if source1[i] == source2[j]:
                    target.append(source1[i])
            else:
                if source1[i] == source2[j] and source1[i] in target == False: 
                    target.append(source1[i])

                
    
    
    return target
                
    
    
        

        
        
            