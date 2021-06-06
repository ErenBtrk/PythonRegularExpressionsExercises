'''
28. Write a Python program to find all words starting with 'a' or 'e' in a given string. 

'''

import re 

str1 = "The following example creates an ArrayList with a capacity of 50 elements. Four "\
       "elements are then added to the ArrayList and the ArrayList is trimmed accordingly.".replace("."," ")

list1 = re.split(" ",str1)
print(list1)
for item in list1:
    if(re.search("^a|^e",item)):
        print(item)