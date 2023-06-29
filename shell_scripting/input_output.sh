#!/bin/bash
echo "Enter filename" #prompts user to enter a filename and read user's input into the 'filename' variable'
read filename

if [ -e $filename ] #-e checks if the file specified by $filename exists
then
	echo "$filename exists in the directory"
	cat $filename
else
	cat > $filename #creates a new file with the name inside $filename, the cmd cat allows user to enter the content of the file which is then saved to the newl created filed
	echo "file created"
fi
