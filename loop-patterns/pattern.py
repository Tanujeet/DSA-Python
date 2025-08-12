#pattern 1
# n=5 
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()



#pattern 2
# n=5
# for i in range(n):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()


#pattern 3
# n=5
# for i in range(n):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


#pattern 4
# n=5
# for i in range(n):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()


#pattern 5
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     print() 


#pattern 6
# n=5
# for i in range(n):
#     for j in range(1,n-i):
#         print(j,end="")
#     print()



#pattern 7
# def pattern7(n):
#     for i in range(n):
#         for j in range(n-i):
#             print(" ",end="")
#         for j in range(1,2*(i+1)):
#             print("*",end="")
#         for j in range(n-i):
#             print(" ",end="")
#         print()



#pattern 8
# def pattern8(n):
#     for i in range(n):
#         for j in range(i):
#             print(" ",end="")
#         for j in range(2*(n-i)-1):
#             print("*",end="")
#         for j in range(i):
#             print(" ",end="")
      
#         print()

# pattern8(5)        

#pattern 9
# def pattern9(n):
#     pattern7(n)
#     pattern8(n)
# pattern9(5)    


#pattern 10
# n=5 
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# for i in range(n-1):
#     for j in range(n-i-1):
#         print("*",end="")
#     print()    


#pattern 11

# n=5
# for i in range(n):
#     start = 1 if i % 2 == 0 else 0
#     for j in range(i+1):
#         print(start,end="")
#         start = 1 - start
#     print()


#pattern 12
# n=5
# for i in range(n):
#     for j in range(1,i+1):
#         print(j,end="")
#     for j in range(1,2*(n-i)-1):
#         print(" ",end="")
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()


#pattern 13
# n = 5  
# num = 1 

# for i in range(1, n + 1):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()


#pattern 14
# n=5
# for i in range(n):
#     for j in range(65,65+i):
#         print(chr(j),end="")
#     print()


#pattern 15
# n=5
# for i in range(n,0,-1):
#     for j in range(65,65+i):
#         print(chr(j),end="")
#     print()


#pattern 16
# n=5
# for i in range(n):
#   ch = chr(65+i)
#   print(ch*(i+1))


#pattern  17
# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(65,65+i):
#         print(chr(j),end="")
#     for j in range(65 + i - 2, 64, -1):
#         print(chr(j), end="")

#     for j in range(n-i-1):
#         print(" ",end="")
#     print()