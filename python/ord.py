#The ord() function in python will return an integer tat represents the unicode character passed
#to it. It takes a single parameter, i.e the below code will return 65
print(ord('A'))

#Typecasting
#implicit typecasting, the python compiler internally typecasts one variable into another type without the external action of the user
int_num = 100
float_num  = 1.01
ans = int_num + float_num
print(type(int_num)) #int
print(type(float_num)) #float
print(type(ans)) #float

#Explicit typecasting the user explicitly forces the compilier to convert a variable from one type to another.i.e
var = 123
newv =(str(var))
print(type(newv)) #string

for i in range(2, 10, 2):
    print(i)
#slicing
my_list = [2, 5, 7, 9, 4, 5, 56, 90]
newl = my_list[2:5]
print(newl)