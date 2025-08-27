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


# Check if the array is sorted

# def is_sorted(arr):
#     n = len(arr)
#     for i in range(1,n):
#         if arr[i] <= arr[i-1]:
#             return False
#     return True         



# print(is_sorted([1, 2, 3, 4]))   
# print(is_sorted([1, 5, 3, 4]))   
# print(is_sorted([10]))          
# print(is_sorted([])) 


# Remove duplicates from Sorted array

#brute approach

# def f(arr):
#     n =len(arr)
#     st = set()
#     for i in range(n):
#         st.add(arr[i])
#     return st    

# arr =[1,1,2,2,2,3,3]
# print(f(arr))