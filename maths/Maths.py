import math 

#Given an integer N, return the number of digits in N.

# n=7789
# count = 0
# while (n > 0):
#    count = count + 1
#    lg = n % 10
#    n= n //10
# print("Your total digits are :",count)


 # If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

# n = 7789
# rev = 0
# while (n>0):
#     lg=n %10
#     rev =(rev * 10) +lg
#     n=n//10
# print(rev)

# Given an integer N, return true if it is a palindrome else return false.

# n = 121
# rev = 0
# dub = n
# while n>0:
#     lg=n %10
#     rev =(rev * 10) +lg
#     n=n//10
# if dub == rev :
#    print(True)
# else:
#    print(False)   


#Given an integer N, return true it is an Armstrong number otherwise return false

# n = 153
# sum =0
# dup = n
# while n > 0 :
#     ld = n % 10
#     sum =  sum + (ld * ld * ld)
#     n = n//10
# print(sum)    
# if dup == sum :
#     print(True)
# else:
#     print(False)        



#Given an integer N, return all divisors of N.


# n = 55
# i = 1
# divisors = []
# while i <= math.sqrt(n):
#     if n % i == 0:
     
#         divisors.append(i)     
#         if i != n // i:     
#           divisors.append(n // i) 
#     i += 1
# divisors.sort()
# print(divisors)


#Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.

# n = 5
# i = 2
# is_prime = True
# while i < n:
#     if n % i == 0:
#         is_prime=False
#         break
#     i += 1
# if is_prime:
#     print("Prime")
# else:
#     print("Not prime")    

