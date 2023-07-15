#!/usr/bin/python3
def substring_extraction(string):
    solution = []
    start = 0 #tracks the start index of the current substring
    s_len = len(string)

    for w in range(1, s_len): #begin from 1, to compare with the prev element
        if string[w] != string[w - 1]: #marks the end of a substring
            if w - start >= 3: #validates the len of the substring
                solution.append([start, w - 1])
            start = w

    #validates whether the last substring has been recorded
    if s_len - start >= 3:
        solution.append([start, s_len - 1])

    return solution

string = 'abedddeeeeaabbbcd'
result = substring_extraction(string)
for substring in result:
    print(substring, ", ", end="")
print()
