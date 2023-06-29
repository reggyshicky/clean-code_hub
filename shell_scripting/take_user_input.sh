#!/bin/bash

echo "Enter a number"
read a

echo "Enter a number"
read b

#prompts user with a customer message, using the flag p
read -p "Enter your age" age

var=$((a+b))
echo $var
echo $age
