#pattern 1
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()


#pattern 2
for i in range(6):
    print("*"*(i))


#pattern 3
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()



#pattern 4
for i in range(6):
    for j in range(1,i+1):
        print(i ,end=" ")
    print()



#pattern 5    
for i in range(5,0,-1):
    print("*" *(i))

#pattern 6
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


#patten 7

for i in range(5):
        for j in range(4,i,-1):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ") 
         
        print()

#pattern 8

n=5
for i in range(n):
     for j in range(i):
        print(" ",end=" ")
     for j in range(2*(n-i)-1):
         print("*",end=" ") 

     print() 


