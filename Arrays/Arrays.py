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



# Brute force approach

# def f(arr):
#     n = len(arr)
#     res = []
#     for i in range(n):
#         if arr[i] not in res:  
#             res.append(arr[i])
#     return res

# arr = [1,1,2,2,2,3,3]
# print(f(arr))   



# better Approach 

# def f(arr):
#     n = len(arr)
#     i = 0
#     for j in range(1,n):
#         if arr[i] !=  arr[j]:
#             arr[i+1]= arr[j]
#             i +=1
#     return i+1        
# arr = [1,1,2,2,2,3,3]
# print(f(arr)) 


# Left Rotate an array by one place

# def f(nums):
#     temp = nums[0]
#     n = len(nums)
#     for i in range(1,n):
#         nums[i-1]=nums[i]
#     nums[n-1]= temp    
#     return nums

# nums=[1,2,3,4,5]
# print(f(nums))


# Left Rotate an array by K place


# def leftRotate(nums, k):
#     n=len(nums)
#     k = k % n
#     nums[:]= nums[-k:]+nums[:-k]
 
#     return nums

# nums=[1,2,3,4,5,6]
# k=2
# print(leftRotate(nums,k))


# moves zero to the end 

# Brute force
# def f(arr):
#     temp=[]
#     n= len(arr)
#     for i in range(n):
#         if arr[i] != 0:
#             temp.append(arr[i])
   
#     for i in range(len(temp)):
#         arr[i]=temp[i]
    

#     nz=len(temp)
#     for i in range(nz,n):
#         arr[i]=0

#     return arr

# arr=[0,1,0,3,12]
# print(f(arr))

#Optimized Approach

# def f(arr):
#     n= len(arr)
#     pos = 0
#     for i in range(n):
#         if arr[i]!=0:
#             arr[pos]=arr[i]
#             pos +=1
#     for i in range(pos,n):
#         arr[i] =0
#     return arr

# arr=[0,0,1,0,12,3]            
# print(f(arr))
    


#linear search

# def f(arr,target):
#     n = len(arr)
#     for i in range(n):
#         if arr[i]== target:
#             return i
#     return -1     

# arr = [1,3,2,6,4]
# target = 6
# print(f(arr,target))


# Find the Union sorted arrays

# def f(arr1,arr2):
#     union =set()
#     for x in arr1:
#         union.add(x)
#     for y in arr2:
#         union.add(y)

#     return sorted(list(union))         

# arr1=[1,1,2,3,4,5]
# arr2=[2,3,4,4,5,6]
# print(f(arr1,arr2))
                 
        


    