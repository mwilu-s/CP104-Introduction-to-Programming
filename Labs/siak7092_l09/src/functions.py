"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-09"
-------------------------------------------------------
"""
# Imports

# Constants


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    
    pc = product_code[:3]
    pi = product_code[3:7]
    pa = product_code[7:10]
    
    return pc, pi, pa


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """
    if len(product_code) < 3:
        category = False;
    else:
        category = product_code[:3].isupper()
    
    if len(product_code[3:7]) < 4:
        digits = False;
    else:
        digits = product_code[3:7].isdigit()
        
    qualifiers = product_code[7:8].isupper()
    
    return category, digits, qualifiers



def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """
    
    if len(password) < 8:
        print("not long enough")
    
    dig = False;
    upper = False;
    lower = False;
    
    for c in password:
        if c.isdigit():
            dig = True;
            break
    
    for c in password:
        if c.isupper():
            upper = True;
            break
    
    for c in password:
        if c.islower():
            lower = True;
            break
        
    
    if dig == False:
        print("no digits")
    
    if upper == False:
        print("no upper case")
        
    if lower == False:
        print("no lower case")
        
    return None
    
    
    
    
def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0
    
    for c in txt:
        if c.isupper():
            uppr = uppr + 1
        elif c.islower():
            lowr = lowr + 1
        elif c.isdigit():
            dgts = dgts + 1
        elif c.isspace():
            whtspc = whtspc + 1
    
    return uppr, lowr, dgts, whtspc


def comma_period_replace(string):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    out = ""
    
    for c in string:
        if c == ",":
            out = out + "."
        else:
            out = out + c
            
    
    return out
            
        