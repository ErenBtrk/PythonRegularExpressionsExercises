'''
19. Write a Python program to search some literals strings in a string.
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'

'''

import re
patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print(f'Searching for "{pattern}" in "{text}"')
    if re.search(pattern,  text):
        print('Matched!')
    else:
        print('Not Matched!')