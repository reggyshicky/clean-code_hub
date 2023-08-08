from sys import argv

if len(argv) == 2:
    print(f"Hello, {argv[1]}") #aspect of indexing, index 1 contains the second argument
else:
    print("Hello World")

#peep this python3 sysArgv.py Reggy : the first argv starts from the name of the file/program you are running, the
#second is Reggy and so forth. 