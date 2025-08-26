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

# c= [64, 25, 12, 22, 11] 
# def f(arr):
#     n = len(c)
#     for i in range(n):
#         min = i
#         for j in range(i+1,n):
#             if arr[j] > arr[min]:
#                 min = j
#         arr[i],arr[min]= arr[min],arr[i]
#     return arr
# print(f(c))


# Count Swaps During Selection Sort

# c=[64, 25, 12, 22, 11] 
# def f(arr):
#     n = len(arr)
#     count=0
#     for i in range(n):
#         min=0
#         for j in range(i+1,n):
#             if arr[j] < arr[min]:
#                 min = j
#         if min != i:
#             arr[i],arr[min] = arr[min],arr[i]
#             count +=1     
#     return arr , count

# sorted_arr, swaps = f(c)
# print("Sorted Array:", sorted_arr)
# print("Total Swaps:", swaps)


#Find Kth Smallest Element

# def f(arr,k):
#     n=len(arr)
#     for i in range(k):
#         min = i
#         for j in range(i+1,n):
#             if arr[j] < arr[min]:
#                 min = j
#         arr[i],arr[min]= arr[min],arr[i]       
                
#     return arr[k-1]



# arr = [7, 10, 4, 3, 20, 15]
# k = 3
# print("Kth Smallest Element:", f(arr, k))


# Bubble Sort

# def f(arr):
#     n = len(arr)
#     flag = True
#     while flag :
#         flag = False
#         for i in range(1,n):
#             if arr[i-1] >  arr[i]:
#                 flag = True
#                 arr[i-1],arr[i]=arr[i],arr[i-1]
#     return arr

# arr= [-5,3,2,1,-3,-3,7,2,2]       
# print(f(arr))