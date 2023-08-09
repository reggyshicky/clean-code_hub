#List Comprehensions
#It is a shorter syntax to create a new list using values of an existing list
a = [0, 1, 2, 3]
#b will store values which are 1 greater than the values stored in a
b = [i + 1 for i in a]
print(b) #[1, 2, 3, 4]
