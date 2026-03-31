"""
-------------------------------------------------------
Word Chain
-------------------------------------------------------
Author:  Mwilu Siakachoma
ID:      169107092
Email:   siak7092@mylaurier.ca
__updated__ = "2024-11-09"
-------------------------------------------------------
"""
# Imports
from functions import has_word_chain
# Constants
words = []
word = input("Enter a word (enter '' to stop): ")

while word != '':
    words.append(word)
    word = input("Enter a word (enter '' to stop): ")

result = has_word_chain(words)
print(result)
