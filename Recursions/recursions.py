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
