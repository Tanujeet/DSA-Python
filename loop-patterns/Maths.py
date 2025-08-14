#extraction of numbers in reverse

n = 7780
while(n>0):
    lastdigit = n % 10
    print(lastdigit)
    n = n//10