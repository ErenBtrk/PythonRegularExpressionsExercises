'''
15. Write a Python program where a string will start with a specific number.

'''

import re
def text_match(text):
        patterns = "^123"
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("123-456"))
print(text_match("456-123"))
print(text_match("12-3123111111111"))