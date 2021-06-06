'''
30. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.

'''
import re

str1 = '21 Ramkrishna Road'
str1 = re.sub("Road$","Rd.",str1)
print(str1)