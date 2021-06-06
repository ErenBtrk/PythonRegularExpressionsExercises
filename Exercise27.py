'''
27. Write a Python program to separate and print the numbers of a given string.

'''

import re

str1 = "Ten 10, Twenty 20, Thirty 30 ,Hundred 100"

print(re.findall("[0-9]{1,}",str1))