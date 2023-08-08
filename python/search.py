def count_characters(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    char_count_string = ""
    for char, count in char_count.items():
        char_count_string += f"{char}{count}"

    # Remove the trailing comma and space
    char_count_string = char_count_string.rstrip(", ")

    return char_count_string


x = count_characters("aaabbbccdeaaa");
print(x);
