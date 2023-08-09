#Set Comprehension
#it is a shorter syntax to create a new set using values of an existing set
a = {0, 1, 2, 3}
#b will store squares of the elements of a
b = {i ** 2 for i in a}
print(b) #output {0, 1, 4, 9}
