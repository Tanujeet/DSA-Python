#pattern 1
# def pattern1(n):
#     for i in range(n):
#         for j in range(n):
#             print("*",end="")
#         print()



#pattern 2
# def pattern2(n):
#     for i in range(n):
#         for j in range(i):
#             print("*",end="")
#         print()


#pattern 3
# def pattern3(n):
#     for i in range(n+1):
#         for j in range(i):
#             print(j+1,end="")
#         print()




#pattern 4
# def pattern4(n):
#     for i in range(n):
#         for j in range(i):
#             print(i,end="")
#         print()


#pattern 5
# def pattern5(n):
#      for i in range(n):
#           for j in range(n-i):
#                print("*",end="")
#           print()



#pattern 6
# def pattern6(n):
#      for i in range(n+1):
#           for j in range(n-i):
#                print(j+1,end="")
#           print()








#pattern 7
# def pattern6(n):
#     for i in range(n):
     
#         for j in range(n - i - 1):
#             print(" ", end="")
    
#         for j in range(2 * i + 1):
#             print("*", end="")
      
#         for j in range(n - i - 1):
#             print(" ", end="")
#         print()





#pattern 8
# def pattern7(n):
#      for i in range(n):
#           for j in range(i):
#                print(" ",end="")
#           for j in range(2*(n-i)-1):
#                print("*",end="")
#           for j in range(i):
#                print(" ",end="")          
#           print()





#pattern 

















def main(n):
    # pattern1(n)
    # pattern2(n)
    # pattern3(n)
    # pattern4(n)
    #  pattern5(n)
     pattern6(n)
    #  pattern7(n)
    #  pattern8(n)
    #  pattern9(n)
main(5)    