'''
17. Write a Python program to check for a number at the end of a string.

'''

import re
def text_match(text):
        patterns = "[0-9]$"
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("123a"))
print(text_match("1234"))
print(text_match("123 "))