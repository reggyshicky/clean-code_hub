import sys
my_dict = {
    "name": "Reggy",
    "Age": 35,
    "School": "TUK"
}
n = input("Enter the name ")
for key, value in my_dict.items():
    if n == value:
        print("Found")
        sys.exit(0)
print("Not found") #if the loops completes without find a match