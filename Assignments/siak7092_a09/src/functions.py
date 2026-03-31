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

def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    line = file_handle.readline()
    counter = 0
    
    while line != "" and counter != count:
        print(line.strip())
        counter = counter + 1
        line = file_handle.readline()
    
    return None


def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    number_list = []
    line = file_handle.readline()
    
    while line != "":
        lst = line.strip().split(",")
        for i in range(len(lst)):
            if i > 0:
                num = int(lst[i])
                if num % 2 == 0:
                    number_list.append(num)
        line = file_handle.readline()
    
    return number_list

def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    line = file_handle.readline()
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    rcount = 0
    
    while line != "":
        for c in line:
            if c.isupper():
                ucount = ucount + 1
            elif c.islower():
                lcount = lcount + 1
            elif c.isdigit():
                dcount = dcount + 1
            elif c.isspace() or c == "\n" or c == "\r" or c == "\n\r":
                wcount = wcount + 1
            else:
                rcount = rcount + 1
        line = file_handle.readline()
    
    return ucount, lcount, dcount, wcount, rcount


def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    line = fh_read.readline()
    lineNum = 0
    
    while line != "":
        fh_write.write(f"[{lineNum}] {line}")
        lineNum = lineNum + 1
        line = fh_read.readline()
        
    return None

def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    line = file_handle.readline()
    std_lst = []
    l_id = ""
    h_id = ""
    total = 0
    count = 0
    lowest = 100
    highest = 0
    
    while line != "":
        std_lst = line.strip().split(",")
        
        if int(std_lst[3]) > highest:
            highest = int(std_lst[3])
            h_id = std_lst[2]
            
        if int(std_lst[3]) < lowest:
            lowest = int(std_lst[3])
            l_id = std_lst[2]
        
        total = total + int(std_lst[3])
        count = count + 1
        line = file_handle.readline()
    
    avg = total/count

    return l_id, h_id, avg
            
        
        
    
                
    
        