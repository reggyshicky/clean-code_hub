#sets are initialized using curly braces
#set removes duplicates items
s = {1, 2, 3}
print(s) #output {1, 2, 3}
s = set([1, 2, 3]) 
print(s) #output {1, 2, 3}
s = {1, 2, 3, 3, 2, 4, 5, 5} 
print(s) #output:{1, 2, 3, 4, 5}

#Inserting a single element into a set using add function of sets
s = {1, 2, 3, 3, 2, 4, 5, 5}
print(s)
s.add(6)
print(s) #{1, 2, 3, 4, 5, 6}
#To insert multple elements into a set, we use the update function and pass a list of elements to be inserted as parameter
s = {1, 2, 3, 3, 2, 4, 5, 5}
s.update([6, 7, 8])
print(s) #output {1, 2, 3, 4, 5, 6, 7, 8}

#Deleting elements from the set
#We can delete elements from a list using either the remove() or the discard() function
s =  {1, 2, 3, 3, 2, 4, 5, 5}
#remove will raise an error if the element is not in the set
s.remove(2)
print(s) #{1, 3, 4, 5}
s.discard(4)
print(s) #{1, 3, 5}

#OPERATORS USED FOR SETS
# Operators What it does
# | (Union) Returns all the unique elements in both the sets.
# & (Intersection) Returns all the elements common to both the sets.
# - (Difference) Returns the elements that are unique to the first set
# ^(Symmetric Difference) Returns all the elements not common to both the set
a = {1, 2, 3, 3, 2, 4, 5, 5}
b = {4, 6, 7, 9, 3}
# Performs the Intersection of 2 sets and prints them
print(a & b)
# Performs the Union of 2 sets and prints them
print(a | b)
# Performs the Difference of 2 sets and prints them
print(a - b)
# Performs the Symmetric Difference of 2 sets and prints them
print(a ^ b)
# Output:
# {3, 4}
# {1, 2, 3, 4, 5, 6, 7, 9}
# {1, 2, 5}
# {1, 2, 5, 6, 7, 9}


