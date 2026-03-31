"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-20"
-------------------------------------------------------
"""
# Imports
from random import random, randint, uniform

# Constants

def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    
    matrix = []
    
    if value_type == 'float':
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(uniform(low,high))
            matrix.append(row)
    
    else:
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(randint(low,high))
            matrix.append(row)
    
    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    rowNum = 0
    colNum = 0
    
    for col in range(len(matrix[0])):
        print(f"{col:>8d}", end="")
    print()
    
    if value_type == "float":
        for col in range(len(matrix)):
            print(f"{col:.0f}", end="")
            
            for row in range(len(matrix[col])):
                print(f"{matrix[col][row]:>8.2f}", end="")
            print()
    
    else:
        for col in range(len(matrix)):
            print(f"{col}", end="")
            
            for row in range(len(matrix[col])):
                print(f"{matrix[col][row]:>8d}", end="")
            print()
                
    return None

def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    s_loc = []
    l_loc = []
    small = 100
    large = 0
    rowIndex = 0
    colIndex = 0
    
    for row in matrix:
        for col in row:
            if col < small:
                small = col
                s_loc = [rowIndex,colIndex]
            
            if col > large:
                large = col
                l_loc = [rowIndex, colIndex]
            
            colIndex = colIndex + 1
        rowIndex = rowIndex + 1
        colIndex = 0
    
    
    return s_loc, l_loc

def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    rowIndex = 0
    colIndex = 0
    
    for row in matrix:
        for col in row:
            replace = num * col;
            matrix[rowIndex][colIndex] = replace
            colIndex = colIndex + 1
        rowIndex = rowIndex + 1
        colIndex = 0
    
    return None

def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    transposed = []
    num = len(matrix[0])
    
    for col in range(num):
        rowReplace = []
        for row in matrix:
            replace = row[col]
            rowReplace.append(replace) 
        
        transposed.append(rowReplace)  

    return transposed
            
    