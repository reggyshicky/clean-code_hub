#!/usr/bin/python3
"""
Implementing linear search in regard to the 0(n) notation
Code performs a linear search on a unsorted list to find the index 
of a given value
"""


def linear_search(data, value):
    for index in range(len(data)):
        if value == data[index]:
            return index
    raise ValueError('Value not found in the list')


if __name__ == "__main__":
    data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
    print(linear_search(data, 7))
