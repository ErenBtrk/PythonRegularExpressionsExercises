'''
2. Write a Python program that matches a string that has an a followed by zero or more b's.

'''

import re
def text_match(text):
        patterns = 'ab+|a0'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))
print(text_match("adab"))
print(text_match("a0ab"))
print(text_match("0a"))

