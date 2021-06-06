'''
29. Write a Python program to separate and print the numbers and their position of a given string.

'''

import re

str1 = "The following example creates an ArrayList with a capacity of 50 elements."\
       "Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
result = re.finditer("[0-9]{1,}",str1)
for match in result:
    print(match.group(),match.span())