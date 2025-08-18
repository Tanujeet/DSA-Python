# Understand Recursion by printing something N times
# def recursion(i,n):
#     if i == n:
#         return
#     print(i)
#     recursion(i+1,n)
# recursion(0,4)        
 


# Print your Name N times using recursion

# def recursion(i,n):
#     if i == n:
#         return
#     print("Harsh")
#     recursion(i+1,n)
# recursion(0,4)        
 


# Print from N to 1 using Recursion


# def recursion(i,n):
#     if i < 1 :
#         return
#     print(i)
#     recursion(i-1,n)
# recursion(5,5)        
 
   


#Given a number ‘N’, find out the sum of the first N natural numbers.


#parameter 

# def sum1(i,sum):
#     if i < 1:
#         print(sum)
#         return
#     sum1(i-1,sum+i)
# sum1(3,0)    


#functional

# def sum2(n):
#     if n == 0:
#         return 0
#     return n + sum2(n-1)

# print(sum2(3))


# Given a number X,  print its factorial.


#functional

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n-1)

# print(fact(3))


#parameter

# def sum1(i,sum):
#     if i < 1:
#         print(sum)
#         return
#     sum1(i-1,sum*i)
# sum1(3,1)    


# you are given an array. The task is to reverse the array and print it.

# def reverse1(arr,l,r):
#     if l >= r:
#         return
#     arr[l],arr[r]=arr[r],arr[l]
#     reverse1(arr,l+1,r-1)


# arr = [1, 2, 3, 4, 5]
# reverse1(arr, 0, len(arr)-1)
# print(arr)


# def reverse2(arr,i,n):
#     if i >= n // 2 :
#         return
#     arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
#     reverse2(arr,i+1,n)

# arr = [1, 2, 3, 4, 5]   
# reverse2(arr,0,len(arr))
# print(arr)