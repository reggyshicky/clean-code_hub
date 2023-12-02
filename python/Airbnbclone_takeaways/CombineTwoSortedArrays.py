# Combining two sorted arrays
# We first initialize two pointers for both the arrays, and create an empty array, we compare the two initial indexes if value of the first pointer
# is less than the value of the second pointer , we append the small value to the array and we increment the pointer, if the value of the second pointer is small than the
# value of the first pointer, we append the value and then increment the second pointer.If one array exhausted we have to make sure the other
#non- exhausted array is appended on the newly created array

def CombineTwoSortedArrays(arr1, arr2):
    newarr = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            newarr.append(arr1[i])
            i += 1
        else:
            newarr.append(arr2[j])
            j += 1
    while i < len(arr1):
        newarr.append(arr1[i])
        i += 1
    while j < len(arr2):
        newarr.append(arr2[j])
        j += 1
    return newarr
        
arr1 = [1,2,3,4,5]
arr2 = [8,9,60,69,81]

result = CombineTwoSortedArrays(arr1, arr2)
print(result)