'''
4. Write a Python program that matches a string that has an a followed by zero or one 'b'.

'''

import re
def text_match(text):
        patterns = 'ab|a0'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("a1c"))
print(text_match("a0"))
print(text_match("bac"))
