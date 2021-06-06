'''
18. Write a Python program to search the numbers (0-9) of length
 between 1 to 3 in a given string.
"Exercises number 1, 12, 13, 345 and 2131 are important"

'''

import re
def text_match(text):
        patterns = "[0-9]{1,3}"
        list1 = re.findall(patterns,  text)
        return list1

print(text_match("Exercises number 1, 12, 13, and 345 are important"))