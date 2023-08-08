while True: # start an infinite loop, the code within this loop will keep running until a break is encountered
    try:
        n = int (input("Height: "))
        if n > 0: # This statement checks whether the value of n is greater than 0.If it is, the break statement is executed which exits the while loop. 
            break # cont: this ensures that the loop will only continue if the user enters a positive integer
    except ValueError:
        print("Not an Integer")

for i in range(n):
    print("#")
    