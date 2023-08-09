def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error, denominator should not be zero")
    finally:
        print("Division completed")

ans = division(4, 0)
print(ans)
ans21 = division(4,2)
print(ans21)

