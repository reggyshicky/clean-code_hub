#!/bin/bash

var1="Apple" #global variable
myfun()
{
	local var2="Banana" #local variable
	var3="cherry" #global variable
	echo "The name of the first fruit is $var1"
	echo "he name of the second fruit is $var2"
}
myfun #calling function 

echo "The name of the first fruit is $var1"
#trying to access local variable
echo "The name of the second fruit is $var2"
echo "The name of the third fruit is $var3"
# when we try to access local variable outside the function its not going to print, coz it is local to function, we use keyword local, by default all variables are global
