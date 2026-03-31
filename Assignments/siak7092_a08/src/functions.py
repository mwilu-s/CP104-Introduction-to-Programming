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

def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    
    spaced = ""
    flag = True;
    
    for c in sentence:
        if flag == True:
            spaced = spaced + c
            flag = False
        
        else:
            if c.isupper():
                spaced = spaced + " " + c.lower()
            else:
                spaced = spaced + c
    
    return spaced 



def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    
    pluralized = ""
    
    if string.endswith("s") or string.endswith("sh") or string.endswith("ch"):
        pluralized = string + "es"
    elif string.endswith("y"):
        if string.endswith("oy") or string.endswith("ay"):
            pluralized = string + "s"
        else:
            pluralized = string[:len(string) -1] + "ies"
    else:
        pluralized = string + "s"
    
    
    return pluralized


def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    suffix = ''
    len1 = len(str1)
    len2= len(str2)
    flag = True;
    
    while len1 >= 0 and len2 >= 0 and flag == True:
        if str1[len1:] == str2[len2:]:
            suffix = str1[len1:]
            flag = True;
            len1 = len1 - 1
            len2 = len2 - 1
        else:
            flag = False;
        
    return suffix
    
    

def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    
    is_valid = True;
    
    if len(isbn) == 17:
        for c in isbn:
            if c.isdigit() or c == '-':
                is_valid = True;
            else:
                is_valid = False;
                
        
        if is_valid == True:
            if isbn[:3] == '978' or isbn[:3] == '979':
                groups = 1
                i = 0
                for i in range(len(isbn)):
                    if isbn[i] == '-' and isbn[i + 1].isdigit():
                        groups = groups + 1
                
                if groups != 5:
                    is_valid = False;
                else:
                    lastDigit = isbn[15:]
                    if lastDigit.find('-') != -1:
                        if lastDigit[1].isdigit():
                            is_valid = True;
                        else:
                            is_valid = False;
                    else:
                        is_valid = False;
                
                
                
    else:
        is_valid = False;
    
    
    return is_valid


def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    word_chain = True;
    i = 0
    
    while i < len(words) - 1 and word_chain == True:
        word1 = words[i]
        word2 = words[i + 1]
        
        if word1[len(word1) - 1:] != word2[0]:
            word_chain = False;
        else:
            i = i+1
            
    return word_chain
    