#extraction of numbers in reverse

# n = 7780
# while(n>0):
#     lastdigit = n % 10
#     print(lastdigit)
#     n = n//10
 
  



#count digits

# n = 7780
# count = 0
# while(n>0):
#     count =count +1
#     n = n//10
#     print("your digit count is :",count)
  


# reverse 
# n=7789
# rev = 0 
# while n>0:
#     ld = n % 10
#     rev = (rev * 10 ) + ld
#     n = n // 10
# print(rev)


#check palindrome
# n=7789
# rev = 0 
# dup = n
# while n>0:
#     ld = n % 10
#     rev = (rev * 10 ) + ld
#     n = n // 10

# if dup == rev :
#     print(True)
# else:
#     print(False)      


#Amrstrong number
n=7789
sum  = 0
dup = n
while n>0:
    ld = n%10
    sum  = sum + (ld * ld * ld)
    n = n // 10
print(sum)    
if dup == sum :
    print(True)
else:
    print(False)        