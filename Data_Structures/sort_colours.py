def sort_colours(string):
    colours = string.split()  # splits the str using the space delimiter
    pos = []  # positions
    sorted_c = []

    for c in colours:
        if not c[-1].isdigit():
            c_name = c[:-1]
            pos.append(float('inf'))
        else:
            c_name = c
            pos.append(int(c[-1]))
        sorted_c.append(c_name)

    for _ in range(len(pos)):
        for x in range(len(pos) - 1):  # bubble sort swapping
            if pos[x] > pos[x + 1]:
                pos[x], pos[x + 1] = pos[x + 1], pos[x]
                sorted_c[x], sorted_c[x + 1] = sorted_c[x + 1], sorted_c[x]

    mod_c = []
    for c in sorted_c:
        mod_c.append(c.rstrip('0123456789'))
        
    solution = ' '.join(mod_c)

    return solution

string1 = "red2 blues black4 green1 gold3"
print("Input:", string1)
print("Output:", sort_colours(string1))

string2 = "gold2 blackI white3"
print("Input:", string2)
print("Output:", sort_colours(string2))
