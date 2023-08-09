#it is a shorter syntax to create a new dictionary using values of an existing dictionay
a = {'Hello':'World', 'First': 1}
#b stores elements of a in value-key pair format
b = {val: k for k, val in a.items()}
print(b) #output {'World': 'Hello', 1: 'First'}

"""
The upper() and lower() converts a string of letters into uppercase or lowercase respectively
The isupper() and islower() functions are used to check if a string is in all uppercase or lowercase respectively, so it returns true or false
isspace() returns True if all characters in string are whitespaces
isalnum() returns True if given string is alphanumeric
isTitle() returns True if string starts with an uppercase letter and then rest of the characters are lowercase
isalpha() returns Ture if given string is alphanumeric
"""
