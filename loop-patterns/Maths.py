#extraction of numbers in reverse

n = 7780
while(n>0):
    lastdigit = n % 10
    print(lastdigit)
    n = n//10
 
  



#count digits

n = 7780
count = 0
while(n>0):
    count =count +1
    n = n//10
    print("your digit count is :",count)
  
