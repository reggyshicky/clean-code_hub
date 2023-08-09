"""
join() takes one argument
join() function merges elements of a list with some delimiter string, and returns the result as a string
"""
list = ["one", "two", "three"]
s = ','.join(list) #you can use any delimiter whether it is space, fullstop, comma, colon, anything
print(s) #output one,two,three

"""Split() function splits the string into a list of substrings (tokens) based on the specified delimiters"""
newlist = s.split(',')
print(newlist) #output ['one', 'two', 'three']