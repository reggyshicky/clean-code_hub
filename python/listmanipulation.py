#changing values in a list

example = ["Sunday", "Monday", "Tuesday", "Wednesday"]
print(example)
example[0] = "Saturday"
print(example)
#['Sunday', 'Monday', 'Tuesday', 'Wednesday']
#['Saturday', 'Monday', 'Tuesday', 'Wednesday']

#delete values from a list
list_ = [5, 7, 10, 95, 38, 43]
del list_[2]
print(list_)  #ouput [5, 7, 95, 38, 43]

#Inserting values in a list
my_list = [7, 18, 95, 32, 65]
my_list.insert(1, 52)
print(my_list) #output is [7, 52, 18, 95, 32, 65]

#Appending values in a list
my_list = [7, 18, 95, 32, 65]
my_list.append(1080)
print(my_list) #output [7, 18, 95, 32, 65, 1080]

#sorting a list, sorting a list means arranging the elements of the list in some particular order
#we sort a list using sort() function
example = ["Reggy", "Shicky", "Betty", "Home"]
print(example) #output ['Reggy', 'Shicky', 'Betty', 'Home']
#sort in ascending order
example.sort()
print(example) #output ['Betty', 'Home', 'Reggy', 'Shicky']
#sort in descending order
example.sort(reverse = True) 
print(example) #output ['Shicky', 'Reggy', 'Home', 'Betty']