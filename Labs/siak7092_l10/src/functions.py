"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-18"
-------------------------------------------------------
"""
# Imports

# Constants

def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int >= 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = []
    line = fh.readline()
    count = 0
    
    while line != "":
        if count == n:
            result = line.strip().split(",")
            break
        line = fh.readline()
        count = count + 1
    return result
    


def number_stats(fh):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """
    line = fh.readline()
    smallest = int(line.strip())
    largest = int(line.strip())
    total = 0
    average = 0
    count = 0
    
    while line != "":
        num = int(line.strip())
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        total = total + num
        count = count + 1
        line = fh.readline()
    
    average = total/count
    return smallest, largest, total, average


def count_frequency_word(fh, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fh.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fh, word)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        word - the word to search for it in fh (str)
    Returns:
        count - the number of appearance of word in fh (int)
    ------------------------------------------------------
    """
    line = fh.readline()
    count = 0
    
    while line != "":
        search = line.strip()
        if search == word:
            count = count + 1
        line = fh.readline()
    
    return count

def find_longest(fh):
    """
    -------------------------------------------------------
    Finds the last word with longest length in fh.
    Assumes file is not empty.
    Use: word = find_longest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the last word with the longest length in fh (str)
    ------------------------------------------------------
    """
    line = fh.readline()
    longLen = len(line.strip())
    word = ""
    
    while line != "":
        search = line.strip()
        if len(search) >= longLen:
            word = search
            longLen = len(word)
        line = fh.readline()
    
    return word


def file_copy(fh_1, fh_2):
    """
    -------------------------------------------------------
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
    Use: file_copy(fh_1, fh_2)
    -------------------------------------------------------
    Parameters:
        fh_1 - source file (file handle - already open for reading)
        fh_2 - target file (file handle - already open for writing)
    Returns:
        None
    ------------------------------------------------------
    """
    line = fh_1.readline()

    while line != "":
        input = line.strip()
        fh_2.write(f"{input}\n")
        line = fh_1.readline()
    
    return None
        
        
        
        