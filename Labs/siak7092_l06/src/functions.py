"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-10-24"
-------------------------------------------------------
"""
# Imports

# Constants
WEEKS = 6

def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(start, finish + 1, increment):
        total += i
    
    return total

def draw_hollow_triangle(width, char):
    """
    -------------------------------------------------------
    Prints a hollow triangle of width characters using
    the char character.
    Use: draw_hollow_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for i in range(width):
        for j in range(i + 1):
            if j==0 or j == i or i == width -1:
                print(char, end ='')
            else:
                print(' ', end = '')
        print()
        
    
    return None

def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print("Age\tSalary\n------------------")
    
    for i in range(age, 66,1):
        print(f"{age}{salary:>16,.2f}")
        age += 1
        salary += salary * (increase/100)
    
    return None


def lumber(b_min, b_max, b_inc, h_min, h_max, h_inc):
    """
    -------------------------------------------------------
    Create a table of the engineering properties of lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated as:
        cross-sectional area = base × height
        moment of inertia = base × height^3 / 12
        section modulus = base × height^2 / 6
    Use: lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
    -------------------------------------------------------
    Parameters:
        b_min - minimum value of base (int > 0)
        b_max - maximum value of base (int > b_min)
        b_inc - increment in base value (int > 0)
        h_min - minimum value of height (int > 0)
        h_max - maximum value of height (int > h_min)
        h_inc - increment in height value (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    print("Base\tHeight\tCross-Sectional Area\tMoment of Inertia\tSection Modulus\n--------------------------------------------------------------------------------")
    
    for i in range(b_min,b_max + 1,b_inc):
        for j in range(h_min, h_max + 1, h_inc):
            csa = i * j
            moi = (i * j**3)/12
            sm = (i * j**2)/6
            print(f"{i:>4d}\tx{j:>4d}{csa:23.2f}{moi:21.2f}{sm:22.2f}")
    

    return None


def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6 week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """
    total_hours = 0
    for i in range(1,WEEKS+1):
        print(f"Week {i}:")
        for j in range(1,ia_count+1):
            hours = float(input(f"Marking hours for IA {j}:"))
            total_hours+=hours
    
    return total_hours  