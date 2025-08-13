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





#pattern9
# def pattern9(n):
#      pattern7(n):
#      pattern8(n):
# pattern9(5)     




#pattern 10
# def pattern10(n):
#      for i in range(n):
#           for j in range(i+1):
#                print("*",end="")
#           print()

#      for i in range(n):
#           for j in range(n-i-1):
#                print("*",end="")
#           print()



#pattern 11
# def pattern11(n):
#      for i in range(n):
         
#           start = 1 if i % 2 == 0 else 0
#           for j in range(i+1):
#               print(start,end="")
#               start = (start + 1) % 2
#           print()
               

    
       






def main(n):
    # pattern1(n)
    # pattern2(n)
    # pattern3(n)
    # pattern4(n)
    #  pattern5(n)
    #  pattern6(n)
    #  pattern7(n)
    #  pattern8(n)
    #  pattern9(n)
    #  pattern10(n)
     pattern11(n)
    #  pattern13(n)
    #  pattern14(n)
    #  pattern15(n)
    #  pattern16(n)
    #  pattern17(n)
main(5)    