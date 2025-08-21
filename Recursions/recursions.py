# Understand Recursion by printing something N times

def f(i,n):
    if i == n:
        return
    print(i)
    f(i+1,n)

f(1,4)  

# Print your Name N times using recursion

  
def f(i,n):
    if i == n:
        return
    print("Harsh")
    f(i+1,n)

f(1,4)  


# Print from N to 1 using Recursion


def f(i,n):
    if i <= 1:
        return
    print(i)
    f(i-1,n)

f(4,4)  



#Given a number ‘N’, find out the sum of the first N natural numbers.

#parameter 

def f(i,sum):
    if i < 1:
        print(sum)
        return
    f(i-1,sum+i)

print(f(4,0))

#functional

def f(n):
    if n == 0:
        return 0
    return n + f(n-1)
print(f(4))



# Given a number X,  print its factorial.


#functional

# def f(i,fact):
#     if i < 1:
#         print(fact)
#         return
#     f(i-1,fact*i)

# f(4,1)




#parameter


# def f(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * f(n-1)
# print(f(4))





# you are given an array. The task is to reverse the array and print it.
# def f(arr,i,l):
#     if i >= l:
#         return 
#     arr[i],arr[l] =arr[l],arr[i]
#     f(arr,i+1,l-1)


# arr=[1,2,3,4,5]
# f(arr,0,len(arr)-1)
# print(arr)



# Given a string, check if the string is palindrome or not."  A string is said to be palindrome if the reverse of the string is the same as the string.


# def f(arr,i,l):
#     if i >= l //2:
#         return True
#     if arr[i] != arr[l-i-1]:
#         return False
#     return f(arr,i+1,l)
 


# arr="MADAM"
# print(f(arr,0,len(arr)))




# Given an integer N. Print the Fibonacci series up to the Nth term

# def f(n):
#     if n <= 1:
#         return n
#     return f(n-1) + f(n-2)
# print(f(6))