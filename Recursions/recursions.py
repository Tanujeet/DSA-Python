# Understand Recursion by printing something N times

# def f(i,n):
#     while i == n:
#         return
#     print(i)
#     f(i+1,n)
# f(0,5)

# Print your Name N times using recursion

# def f(i,n):
#     while i == n:
#         return
#     print("Harsh")
#     f(i+1,n)
# f(0,5)


# Print from N to 1 using Recursion

# def f(i,n):
#     while i <= 1:
#         return
#     print(i)
#     f(i-1,n)
# f(5,5)


   


#Given a number ‘N’, find out the sum of the first N natural numbers.


#parameter 

# def f(i,n, sum):
#     if i > n:
#         print(sum)
#         return
#     f(i+1,n,sum+i)
# n = 3
# f(1,n,0)

#functional

# def f(n):
#     if n == 0: 
#         return 0
#     return n + f(n-1)


# N = 5
# print(f(N))



# Given a number X,  print its factorial.


#functional
# def f(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * f(n-1)

# print(f(3))

#parameter

# def f(i,fact):
#     if i < 1:
#         print(fact)
#         return
#     f(i-1,fact*i)
# f(3,1)


# you are given an array. The task is to reverse the array and print it.

# def f(arr,i,l):
#     if i >=l:
#         return
#     arr[i],arr[l]=arr[l],arr[i]
#     f(arr,i+1,l-1)
                
# arr=[1,2,3,4,5]
# f(arr,0,len(arr)-1)
# print(arr)


# def reverse2(arr,i,n):
#     if i >= n // 2 :
#         return
#     arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
#     reverse2(arr,i+1,n)

# arr = [1, 2, 3, 4, 5]   
# reverse2(arr,0,len(arr))
# print(arr)




# Given a string, check if the string is palindrome or not."  A string is said to be palindrome if the reverse of the string is the same as the string.

# def f(arr,i,n):
#     if i >= n //2:
#         return True
#     if arr[i] != arr[n-i-1]:
#         return False
#     return f(arr, i + 1, n)
    
# arr="MADAM"
# print(f(arr,0,len(arr)))