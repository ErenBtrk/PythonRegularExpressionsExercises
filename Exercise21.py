'''21. Write a Python program to find the substrings within a string. Go to the editor

Sample text :

'Python exercises, PHP exercises, C# exercises'

Pattern :

'exercises'

Note: There are two instances of exercises in the input string.

'''

import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print(f'Found "{match}"')