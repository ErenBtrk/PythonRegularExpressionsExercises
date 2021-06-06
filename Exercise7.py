'''
7. Write a Python program to find sequences of lowercase letters joined with a underscore.

'''

import re

def findSequences(text):
    return re.findall("[a-z]_",text)

str1 = input("Please enter a string : ")

print(findSequences(str1))