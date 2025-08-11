# pattern 1
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()



# #pattern 2
# n=5
# for i in range(n):
#     for j in range(i+1):
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
#     for j in range(n-1-i):
#         print("*",end="")
#     print()


#pattern 6
# n=5
# for i in range(n):
#     for j in range(1,n-i-1):
#         print(j,end="")
#     print()

#pattern 7

# def pattern7(n):
#     for i in range(n):
#         for j in range(n-1-i):
#             print(" ",end="")
#         for j in range(2*i+1):
#             print("*",end="")
#         for j in range(n-1-i):
#             print(" ",end="")        
#         print()


#pattern 8
# def pattern8(n):
  
#     for i in range(n):
#         for j in range(i):
#             print(" ",end="")
#         for j in range(2*(n-1-i)+1):
#             print("*",end="")
#         for j in range(i):
#             print(" ",end="")
            
#         print()

#pattern 9

# def pattern9(n):
#     pattern7(n)
#     pattern8(n)

# pattern9(5)     


