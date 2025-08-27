# Largest Element in an Array

# def f(arr):
#     largest = arr[0]
#     n = len(arr)
#     for i in range(n):
#         if arr[i] > largest:
#             largest = arr[i]
#     return largest

# arr = [1,2,4,5,1]
# print(f(arr))        


# second largest element in the array 

#Better approach

# def f(arr):
#     largest = arr[0]
#     slargest =-1
#     n = len(arr)
#     for i in range(n):
#         if arr[i] > largest:
#             largest = arr[i]
    
#     for i in range(n):
#         if arr[i]> slargest and arr[i] != largest:
#             slargest = arr[i]

#     return largest,slargest


# arr = [1,2,4,5,1]

# print(f(arr))

#optimal approach

# def f(arr):
#     largest = arr[0]
#     slargest = -1
#     n = len(arr)
#     for i in range(n):
#         if arr[i] > largest:
#             slargest = largest
#             largest = arr[i]
#         elif arr[i] < largest and arr[i] > slargest :
#             slargest = arr[i]

#     return largest,slargest



# arr = [1,2,4,5,1]
# print(f(arr))