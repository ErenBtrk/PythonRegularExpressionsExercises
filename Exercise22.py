'''
22. Write a Python program to find the occurrence and position of the substrings within a string

'''

import re

str1 = "Hello World.This is yarasa reis calling.yarasa"
result = re.finditer("yarasa",str1)
for match in result:
    print(match.group(),match.span())


    