#!/usr/bin/python3
"""Module doc for using **kwargs and *args to call a function"""


def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# Now you can use *args and **kwargs to pass arguments
# Here is how to do it

# first with *args


args = ("two", 3, 5)
test_args_kwargs(*args)
"""
arg1: two
arg2: 3
arg3: 5
"""
# Now with **kwargs


kwargs = {"arg3": 3, "arg2": "two", "arg1":5}
test_args_kwargs(**kwargs)
"""
arg1: 5
arg2: two
arg3: 3
