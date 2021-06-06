'''
3. Write a Python program that matches a string that has an a followed by one or more b's.

'''

import re
def text_match(text):
        patterns = 'ab+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("abb"))
print(text_match("abbb"))
print(text_match("abbbb"))
print(text_match("acb"))
print(text_match("bac"))