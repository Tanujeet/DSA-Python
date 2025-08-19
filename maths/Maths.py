import math 

#Given an integer N, return the number of digits in N.

n=7789
count = 0
while n > 0:
    ld = n % 10
    n = n // 10
    count +=1
print(count)    

# If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

n= 7789
rev = 0
while n > 0:
    ld = n % 10
    rev = rev * 10 + (ld)
    n = n //  10
print(rev)
 


# Given an integer N, return true if it is a palindrome else return false.

n=7789
rev = 0
dup = n
while n > 0:
    ld = n % 10
    rev = rev * 10 + (ld)
    n = n //  10
if dup == rev:
    print(True)
else:
    print(False)    
 

#Given an integer N, return true it is an Armstrong number otherwise return false

n= 521
sum = 0
dup = n
while n > 0:
    ld = n % 10
    sum = sum + (ld*ld*ld)
    n = n //  10
if sum == dup:
    print(True)
else:
    print(False)        


#Given an integer N, return all divisors of N.

n = 7789
i=1
divisior = []
while i <= math.sqrt(n):
    if n % i:
        divisior.append(i)
        if i !=n // i:
            divisior.append(n//i)
      
    i +=1
divisior.sort()
print(divisior)    


#Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.

n = 7789
i=2
is_prime = True
while i <= n:
    if n % i ==0:
        is_prime=False
        break
    i+=1
if is_prime:
    print(True)
else:
    print(False)        
     

# Given two integers N1 and N2, find their greatest common divisor.

n1=12
n2=9
i = min(n1,n2)
while i >= 1:
    if n1 % i == 0 and n2 % i == 0:
        print(i)
        break
    i-=1

#Euclidean algorithm

n1=12
n2=9
while n2 != 0:
    n1,n2=n2,n1%n2
print(n1)    