'''
23. Write a Python program to replace whitespaces with an underscore and vice versa.

'''
import re 

def multiple_replace(dict, text):
  # Create a regular expression  from the dictionary keys
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text) 

if __name__ == "__main__": 

  text = "Hello_ World_.This_ is_ Yarasa_ Reis_ Calling_."

  dict = {
    " " : "_",
    "_" : " "
  } 

  print( multiple_replace(dict, text))
