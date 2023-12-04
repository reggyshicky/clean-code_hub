# given abcde and ace , ace is a subsequent of abcde meaning subsequence of 
# a string is a sequence of characters that can be obtained by deleting some 
# (or none) of the characters from the original string, while maintaining the 
# relative order of the remaining characters. For example, "ace" is a 
# subsequence of "abcde" while "aec" is not. 
# We wll initialize two pointers, and then we will iterate through the two strings, if a letter in ace is in abcde, we move the index of ace to the next inde
# indexes of abcde we continue moving regardless, if a letter of ace is not in abcde, we continue moving the index of abcde, till we find it
#....more on the code

def  Subsequence(subsequence, originalstring):
    i = 0
    j = 0
    while (i < len(subsequence) and j < len(originalstring)):
        if subsequence[i] == originalstring[j]:
            i += 1
        j += 1
    return i == len(subsequence)

Subsequencestring = "ai"
fullstring = "manequin"

print(Subsequence(Subsequencestring, fullstring))