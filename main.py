def f(n):
    for i in range(2,n):
       if i % 1 == 0:
           i+=1
           print(i)

n = 10
f(n)