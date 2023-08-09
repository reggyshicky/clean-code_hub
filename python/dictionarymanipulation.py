#printing keys and valies in dictionaries
#To print the keys of the dictionary use the .keys() method and to print the values
#use the .values() method

dict = {'first' : 'sunday', 'second' : 'monday', 'third' : 'tuesday'}
#print keys
for key in dict.keys():
    print(key) #output : first, second, third

#print values
for value in dict.values():
    print(value) #output: sunday, monday, tuesday


#UPDATE KEY VALUE IN DICTIONARY
#Update key value which is not present in dictionary
dict = {'first' : 'sunday', 'second' : 'monday', 'third' : 'tuesday'}
for item in dict.items():
    print(item)
dict['fourth'] = 'wednesday'
for item in dict.items():
    print(item)
#Output:
# ('first', 'sunday')
# ('second', 'monday')
# ('third', 'tuesday')
# ('first', 'sunday')
# ('second', 'monday')
# ('third', 'tuesday')
# ('fourth', 'wednesday')

#DELETE KEY-VALUE PAIR FROM DICTIONARY
#We can delete a key-value pair from a dictionary using the del keyword followed by key value to be deleted enclosed in  []
dict = {'first' : 'sunday', 'second' : 'monday', 'third' : 'tuesday'}
for item in dict.items():
    print(item)
del dict['third']
for item in dict.items():
    print(item)
# Output:
# ('first', 'sunday')
# ('second', 'monday')
# ('third', 'tuesday')
# ('first', 'sunday')
# ('second', 'monday')

#Upadate key value which is not present in dictionary
dict = {'first' : 'sunday', 'second' : 'monday', 'third' : 'tuesday'}
for item in dict.items():
    print(item)
dict['third'] = 'wednesday'
for item in dict.items():
    print(item)
# Output:
# ('first', 'sunday')
# ('second', 'monday')
# ('third', 'tuesday')
# ('first', 'sunday')
# ('second', 'monday')
# ('third', 'wednesday')

#MERGE 2 DICTIONARIES
#We can merge 2 dictionaries int 1 by using the update() method
dict1 = {'first': 'sunday', 'second': 'monday', 'third': 'tuesday' }
dict2 = {1: 3, 2: 4, 3: 5}
dict1.update(dict2)
print(dict1) #output {'first': 'sunday', 'second': 'monday', 'third': 'tuesday', 1: 3, 2: 4, 3: 5}