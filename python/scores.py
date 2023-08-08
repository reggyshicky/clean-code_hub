#use of lists
scores = []
for i in range (3):
    n = int(input("Please input the scores "))
    scores.append(n)
    #alternative of appending is scores += [n]
average = sum(scores) / len(scores)
print("The average is {}".format(average))
#Note that append() method of a list in python does not return the modified list, instead it directly modifies the list in place and returns None