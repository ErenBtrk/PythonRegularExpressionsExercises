'''
1. Write a Python program to check that a string contains 
only a certain set of characters (in this case a-z, A-Z and 0-9).

'''

import re

try:
    str1 = input("Please enter a string which only contains a-z,A-Z and 0-9 : ")
    if(not re.search("[a-z]",str1)):
        raise Exception("The string does not contain a-z")
    if(not re.search("[A-Z]",str1)):
        raise Exception("The string does not contain A-Z")
    if(not re.search("[0-9]",str1)):
        raise Exception("The string does not contain 0-9")
except Exception as excObject:
    print(excObject)
else:
    print("The string contains a-z,A-Z,0-9")

##############################################################

import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))