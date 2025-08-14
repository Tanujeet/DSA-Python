#pattern 1
def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()



#pattern 2
def pattern2(n):
    for i in range(n):
        for j in range(i):
            print("*",end="")
        print()


#pattern 3
def pattern3(n):
    for i in range(n+1):
        for j in range(i):
            print(j+1,end="")
        print()




#pattern 4
def pattern4(n):
    for i in range(n):
        for j in range(i):
            print(i,end="")
        print()


#pattern 5
def pattern5(n):
     for i in range(n):
          for j in range(n-i):
               print("*",end="")
          print()



#pattern 6
def pattern6(n):
     for i in range(n+1):
          for j in range(n-i):
               print(j+1,end="")
          print()








#pattern 7
def pattern7(n):
    for i in range(n):
     
        for j in range(n - i - 1):
            print(" ", end="")
    
        for j in range(2 * i + 1):
            print("*", end="")
      
        for j in range(n - i - 1):
            print(" ", end="")
        print()





#pattern 8
def pattern8(n):
     for i in range(n):
          for j in range(i):
               print(" ",end="")
          for j in range(2*(n-i)-1):
               print("*",end="")
          for j in range(i):
               print(" ",end="")          
          print()





#pattern9
def pattern9(n):
     pattern7(n)
     pattern8(n)




#pattern 10
def pattern10(n):
     for i in range(n):
          for j in range(i+1):
               print("*",end="")
          print()

     for i in range(n):
          for j in range(n-i-1):
               print("*",end="")
          print()



#pattern 11
def pattern11(n):
     for i in range(n):
         
          start = 1 if i % 2 == 0 else 0
          for j in range(i+1):
              print(start,end="")
              start = (start + 1) % 2
          print()
               

    
#pattern 12
def pattern12(n):
     for i in range(1,n+1):
          for j in range(1,i+1):
               print(j,end="")
          for j in range(2*(n-i)):
               print(" ",end="")
          for j in range(i,0,-1):
               print(j,end="")
          print()
       

#pattern 13
def pattern13(n):
     count =1
     for i in range(n):
          for j in range(i+1):
               print(count,end=" ")
               count = count + 1
          print()




#pattern 14
def pattern14(n):
     for i in range(n):
          for j in range(i+1):
               print(chr(65+j),end="")
          print()




#pattern 15
def pattern15(n):
     for i in range(n):
          for j in range(n-i):
               print(chr(65+j),end="")
          print()




#pattern 16 
def pattern16(n):
     for i in range(n):
          for j in range(i+1):
               print(chr(65+i),end="")
          print()




#pattern 17
def pattern17(n):
     for i in range(1,n):
          for j in range(n-i):
               print(" ",end="")
          for j in range(i):
               print(chr(65 + j),end="")
          for j in range(i-2,-1,-1):
               print(chr(65 + j),end="")
          for j in range(n-i):
               print(" ",end="")
          print()


#pattern 18


#pattern 19.1
def pattern191(n):
     for i in range(n):
          for j in range(n-i): 
               print("*",end="")
          for j in range(2*i): 
               print(" ",end="")
          for j in range(n-i): 
               print("*",end="")
          print()




# pattern 19.2
def pattern192(n):
     for i in range(n):
          for j in range(i+1):
               print("*",end="")
          for j in range(2*(n-i-1)):
               print(" ",end="")
          for j in range(i+1):
               print("*",end="")
          print()







# pattern 19
def pattern19(n):
     pattern191(n)
     pattern192(n)



#pattern 20
def pattern20(n):
     pattern192(n)
     pattern191(n)



#pattern 21
def pattern21(n):
     for i in range(n-1):
          for j in range(n-1):
               print("*",end="")
          print()





















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
    #  pattern11(n)
    #  pattern12(n)
    #  pattern13(n)
    #  pattern14(n)
    #  pattern15(n)
    #  pattern16(n)
    #  pattern17(n)
    #  pattern18(n)
 #  pattern19(n)
#   pattern20(n)  
  pattern21(n) 
 #   pattern22(n)
main(5)    