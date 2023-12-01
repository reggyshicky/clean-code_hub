def SumTwoNumber_Target(arr, target):
    left = 0
    right = len(arr) - 1
    # Two pointers logic
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == target:
            return True
        elif currentSum < target:
             left += 1
        else:
            right -= 1
    return False
        

print(SumTwoNumber_Target([1,2,3,4,5], 5))
print(SumTwoNumber_Target([1,2,3,4,5], 50))