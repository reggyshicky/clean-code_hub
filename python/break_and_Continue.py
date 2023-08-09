#break statements are used to break out of the current loop and allow execution of
#of the next statement, break terminates the loop prematurely
for i in range(5):
    if i == 3:
        break  #this code will only print 0, 1, 2
    print(i)

#continue statement allows us to send the control back to the starting of the loop, skipping all the lines of code below in the loop
for i in range(5):
    if i == 3:
        continue
    print(i)


def func():
    global value
    value = "Local"
value = "Global"
func()
print(value)
#Output: Local
#To modify global variable from inside a function, we use global statement
#we set the "value" as Global.To change its value from inside the function, we use the global keyword along with 'value' to change its value to local and then print it
 