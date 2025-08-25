from collections import Counter

#  Given an array, we have found the number of occurrences of each element in the array.

# def frequency(arr,n):
#     mp={}
#     for n in arr:
#         mp[n] = mp.get(n,0)+1
#     print(mp)    
        
# arr=[10,5,15,10,5]
# n=len(arr)
# frequency(arr,n)


# Given an array of size N. Find the highest and lowest frequency element.

# def f(arr):
#   freq = Counter(arr)
#   maxelement = max(freq,key = freq.get)
#   minelement = min(freq,key = freq.get)
#   return (maxelement,minelement)

# arr=[2,2,2,3,4,4]
# print(f(arr))


#two sum 

# def f(nums,target):
#     map={}
#     for i , num in enumerate(nums):
#         complement = target- num
#         if complement in map:
#             return [map[complement],i]
#         map[num] = i 
     

# nums=[2,7,11,15]
# target=9
# print(f(nums,target))

#First Unique Character in a String


