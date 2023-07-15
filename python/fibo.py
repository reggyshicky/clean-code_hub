#!/usr/bin/python3
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')  # write fibonacci series upto n
        a, b = b, a + b
    print()


def fib2(n):  # return fibonacci series upto n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

# how to make a module, then on the terminal enter python3 to access python interpreter, then import fibo, (comes from fibo.py)... and then use fibo.fib(arg) to call your function, the same tofibo.fib2(arg). if you using a function more often, you ca always do this >>>fib = fibo.fib  and then >>>fib(arg)
