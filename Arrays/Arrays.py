import math


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


# brute force

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
                 
        
#optimal approach
# def f(arr1, arr2):
#     n1 = len(arr1)
#     n2 = len(arr2)
#     i = 0
#     j = 0
#     unionArr = []

#     while i < n1 and j < n2:
#         if arr1[i] <= arr2[j]:
#             if len(unionArr) == 0 or unionArr[-1] != arr1[i]:
#                 unionArr.append(arr1[i])
#             i += 1
#         else:
#             if len(unionArr) == 0 or unionArr[-1] != arr2[j]:
#                 unionArr.append(arr2[j])
#             j += 1

#     # Baaki bache huye elements add karo
#     while i < n1:
#         if len(unionArr) == 0 or unionArr[-1] != arr1[i]:
#             unionArr.append(arr1[i])
#         i += 1

#     while j < n2:
#         if len(unionArr) == 0 or unionArr[-1] != arr2[j]:
#             unionArr.append(arr2[j])
#         j += 1

#     return unionArr


# # Example
# arr1 = [1,1,2,3,4,5]
# arr2 = [2,3,4,4,5,6]
# print(f(arr1, arr2))


#intersection of sorted Arrays


# def intersection(arr1,arr2):
#     n = len(arr1)
#     m = len(arr2)
#     i = 0
#     j = 0
#     ans=[]
#     while i < n and j < m:
#         if arr1[i] < arr2[j]:
#             i+=1
#         elif arr2[j] <arr1[i]:
#             j +=1

#         else:
#             ans.append(arr1[i])
#             i+=1
#             j+=1
#     return ans


# arr1=[4,9,5]
# arr2=[9,4,9,8,4]
# print(intersection(arr1,arr2))

  

#missing number



#Brute force

# def f(arr1):
#     n = len(arr1)

#     for i in range(n):
#         flag = 0
#         for j in range(n-1):
#             if arr1[j] == i:
#                 flag=1
#                 break
#     if flag == 0:
#         return i        
    
# arr1=[1,2,4,5]
# print(f(arr1))    


# optimal approach
# def f(arr):
#     n = len(arr)
#     s1= n * n+1 %2
#     s2 =0
#     for i in range(n):
#         s2 = arr[i]

#     return s1-s2    


# arr=[1,2,4,5]
# print(f(arr))


#Maxium consectuve number

# def f(arr):
#     count=0
#     maxi =0 
#     n = len(arr)
#     for i in range(n):
#         if arr[i]==1:
#             count +=1
#             maxi = max(maxi,count)
#         else:
#             count =0

#     return maxi


# arr=[1,1,0,1,1,1,0,1]            
# print(f(arr))



#longest subarray with sum k

# brute force    
# def f(arr,k):
#     n=len(arr)
#     maxl=0
#     for i in range(n):
#         for j in range(i,n):
#             s=0
#             for x in range(i,j+1):
#                 s+=arr[x]
#             if s == k:
#                 maxl = max(maxl,j-i+1)
#     return maxl

# arr=[2,3,5,1,9]
# k=10
# print(f(arr,k))


#better 

# def f(arr, target):
#     n = len(arr)
#     maxl = 0
#     for i in range(n):
#         s = 0
#         for j in range(i, n):
#             s += arr[j]   # direct sum karte jao
#             if s == target:
#                 maxl = max(maxl, j - i + 1)
#     return maxl

# arr = [2, 3, 5, 1, 9]
# k = 10
# print(f(arr, k))  # 3


#optimal 

# def longest_subarray_sum_k(arr, k):
#     n = len(arr)
#     prefix_sum = 0
#     mp = {}  # prefix_sum -> index
#     max_len = 0

#     for i in range(n):
#         prefix_sum += arr[i]

#         # agar pura prefix hi k hai
#         if prefix_sum == k:
#             max_len = max(max_len, i + 1)

#         # agar prefix_sum - k pehle aa chuka hai
#         rem = prefix_sum - k
#         if rem in mp:
#             max_len = max(max_len, i - mp[rem])

#         # sirf pehli baar store karte hain (shortest index rakho)
#         if prefix_sum not in mp:
#             mp[prefix_sum] = i

#     return max_len


# arr = [2, 3, 5, 1, 9]
# k = 10
# print(longest_subarray_sum_k(arr, k))  # Output: 3 (subarray [2,3,5])



# Kadane's Algorithm : Maximum Subarray Sum in an Array

# def f(arr):
#     n = len(arr)
#     maxi = -math.inf
#     sum = 0
#     for i in range(n):
#         sum += arr[i]
#         if sum > maxi:
#             maxi=sum
#         if sum < 0:
#             sum = 0
#         if maxi < 0:
#             maxi=0


#         i+=1
      


#     return maxi


# arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(f(arr))



# Stock Buy and Sell

# def maxProfit(arr):
#     maxPro = 0
#     minPrice = float('inf')
#     for i in range(len(arr)):
#         minPrice = min(minPrice, arr[i])
#         maxPro = max(maxPro, arr[i] - minPrice)
#     return maxPro

# arr = [7, 1, 5, 3, 6, 4]
# maxPro = maxProfit(arr)
# print("Max profit is:", maxPro)



#Rearrange array elements by sign

# def f(arr):
#     n=len(arr)
#     posIndex=0
#     negIndex=1
#     ans=[0]*n
#     for i in range(n):
#         if arr[i] < 0:
#             ans[negIndex]=arr[i]
#             negIndex +=2
#         else:
#             ans[posIndex]=arr[i]
#             posIndex +=2

#     return ans        


# arr=[3,1,-2,-5,2,-4]
# print(f(arr))


  
# Longest Consecutive Sequence 


# def longestSuccessiveElements(a):
#     n = len(a)
#     if n == 0:
#         return 0

#     longest = 1
#     st = set()
#     # put all the array elements into set
#     for i in range(n):
#         st.add(a[i])

#     # Find the longest sequence
#     for it in st:
#        
#         if it - 1 not in st:
#     
#             cnt = 1
#             x = it
#             while x + 1 in st:
#                 x += 1
#                 cnt += 1
#             longest = max(longest, cnt)
#     return longest

# a = [100, 200, 1, 2, 3, 4]
# ans = longestSuccessiveElements(a)
# print("The longest consecutive sequence is", ans)



# Set Matrix Zeroes 

# def f(m, n, arr):
#     row = [0] * m
#     col = [0] * n
    
#     for i in range(m):
#         for j in range(n):
#             if arr[i][j] == 0:
#                 row[i] = 1
#                 col[j] = 1
    
#     for i in range(m):
#         for j in range(n):
#             if row[i] == 1 or col[j] == 1:
#                 arr[i][j] = 0

#     return arr
         
# arr = [
#   [1, 2, 3],
#   [4, 0, 6],
#   [7, 8, 9]
# ]
# print(f(3, 3, arr))


#rotate Matrix / image by 90 degrees

# def f(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(i):
#             arr[i][j],arr[j][i]=arr[j][i], arr[i][j]
#     for i in range(n):
#         arr[i].reverse()
#     return arr            

# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(f(arr))        


# Spiral Traversal of a Matrix

# def printSpiral(mat):
    
#     ans = []
 
#     n = len(mat)
#     m = len(mat[0]) 
  
    
#     top = 0
#     left = 0
#     bottom = n - 1
#     right = m - 1

   
#     while (top <= bottom and left <= right):
     
#         for i in range(left, right + 1):
#             ans.append(mat[top][i])

#         top += 1

      
#         for i in range(top, bottom + 1):
#             ans.append(mat[i][right])

#         right -= 1

#         if (top <= bottom):
#             for i in range(right, left - 1, -1):
#                 ans.append(mat[bottom][i])

#             bottom -= 1

      
#         if (left <= right):
#             for i in range(bottom, top - 1, -1):
#                 ans.append(mat[i][left])

#             left += 1

#     return ans


# mat = [[1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [9, 10, 11, 12],
#        [13, 14, 15, 16]]
                     
# ans = printSpiral(mat)

# print(ans)

#pascal triangle

# def generateRow(row):
#     ans = 1
#     ansRow = [1] #inserting the 1st element
    
#     #calculate the rest of the elements:
#     for col in range(1, row):
#         ans = ans * (row - col)
#         ans = ans // col
#         ansRow.append(ans)
#     return ansRow

# def pascalTriangle(n):
#     ans = []
    
#     #store the entire pascal's triangle:
#     for row in range(1, n+1):
#         ans.append(generateRow(row))
#     return ans

# if __name__ == '__main__':
#     n = 5
#     ans = pascalTriangle(n)
#     for it in ans:
#         for ele in it:
#             print(ele, end=" ")
#         print()

# n/3 element

def f(arr):
    n= len(arr)
    cnt1=0
    cnt2=0
    el1=None
    el2=None

    for i in range(n):
        if cnt1 == 0 and el2 != arr[i] :
            cnt1=1
            el1=arr[i]
        elif cnt2 == 0 and el1 != arr[i]:
            cnt2 =1
            el2=arr[i]    
        elif el1 == arr[i]:
            cnt1 +=1
        elif el2 == arr[i]:
            cnt2 +=1     
        else:
            cnt1 -=1    
            cnt2 -=1    
    
    ans=[]
    for candidate in [el1,el2]:
        if candidate is not None and arr.count(candidate) >  n // 3:
            ans.append(candidate)

    return ans

arr=[2,2,1,3,1,1,3,1,1]
print(f(arr))