# selection sort 

# ascending order

# c= [64, 25, 12, 22, 11] 
# def f(arr):
#     n = len(c)
#     for i in range(n):
#         min = i
#         for j in range(i+1,n):
#             if arr[j] < arr[min]:
#                 min = j
#         arr[i],arr[min]= arr[min],arr[i]
#     return arr
# print(f(c))        


# decending order

c= [64, 25, 12, 22, 11] 
def f(arr):
    n = len(c)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j] > arr[min]:
                min = j
        arr[i],arr[min]= arr[min],arr[i]
    return arr
print(f(c))


# Count Swaps During Selection Sort

c=[64, 25, 12, 22, 11] 
def f(arr):
    n = len(arr)
    count=0
    for i in range(n):
        min=0
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i],arr[min] = arr[min],arr[i]
            count +=1     
    return arr , count

sorted_arr, swaps = f(c)
print("Sorted Array:", sorted_arr)
print("Total Swaps:", swaps)


#Find Kth Smallest Element

def f(arr,k):
    n=len(arr)
    for i in range(k):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min]= arr[min],arr[i]       
                
    return arr[k-1]



arr = [7, 10, 4, 3, 20, 15]
k = 3
print("Kth Smallest Element:", f(arr, k))


# Bubble Sort

# asending order

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



arr= [-5,3,2,1,-3,-3,7,2,2]       
print(bubble_sort(arr))


#descending order

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



arr= [-5,3,2,1,-3,-3,7,2,2]       
print(bubble_sort(arr))


# check if array is already sorted or not 

def f(arr):
    n = len(arr)
    for i in range(n):
        flag = False
        for j in range(0,n-i-1):
            if arr [j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag = True
    if flag:
        print("Array was NOT sorted")
    else :
        print("Array is already sorted")
  


arr=[1,2,3,4,5]
print(f(arr))       

#Bubble Sort a nearly sorted array Try counting number of swaps needed

def bubble_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count +=1
    return arr,count




# arr=[1,2,3,5,4]          
# sorted_arr, swaps = bubble_sort(arr)
# print("Sorted Array:", sorted_arr)
# print("Total Swaps:", swaps)



# insertion sort

# def f(arr):
#     n= len(arr)
#     for i in range(n):
#         for j in range(i,0,-1):
#             if arr[j-1] > arr[j]:
#                 arr[j-1],arr[j]= arr[j],arr[j-1]
#             else:
#                 break
#     return arr        


# arr= [-5,3,2,1,-3,-3,7,2,2]           
# print(f(arr))     



# total number of swaps happended

# def f(arr):
#     n= len(arr)
#     count = 0
#     for i in range(n):
#         for j in range(i,0,-1):
#             if arr[j-1] > arr[j]:
#                 arr[j-1],arr[j]= arr[j],arr[j-1]
#                 count += 1
#             else:
#                 break
#     return arr,count        


# arr= [-5,3,2,1,-3,-3,7,2,2]
# inserted_arr,swap = f(arr)
# print("Sorted Array",inserted_arr)         
# print("Swaps taken",swap)         
  

# After inserting each element into the sorted part of the array, print the current state of the array.
  
# def insertion_sort_verbose(arr):

#     n = len(arr)
#     swap_count = 0

#     for i in range(1, n):
#         for j in range(i, 0, -1):
#             if arr[j-1] > arr[j]:
#                 arr[j-1], arr[j] = arr[j], arr[j-1]  # Swap
#                 swap_count += 1
#             else:
#                 break
#         print(f"Array after inserting element at index {i}: {arr}")

#     print("\nSorted Array:", arr)
#     print("Total swaps:", swap_count)
#     return arr, swap_count


# arr = [4, -1, 7, 3, 0, -5, 2]
# insertion_sort_verbose(arr)



#Merged Sort / Divide and conquerer algo

# Quick sort 

# def f(arr):
#     if len(arr) <= 1:
#         return arr

#     p = arr[-1]  # pivot = last element
#     L = [x for x in arr[ :-1] if x <= p]   # left subarray
#     R = [x for x in arr[ :-1] if x > p]   # right subarray

#     L = f(L)   # recursive sort left
#     R = f(R)   # recursive sort right

#     return L + [p] + R


# arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
# print(f(arr))
