# Largest Element in an Array

def f(arr):
    largest = arr[0]
    n = len(arr)
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
    return largest

arr = [1,2,4,5,1]
print(f(arr))        