# def f(arr):
#      for i in range(len(arr)):
#           min = i
#           for j in range(i+1,len(arr)):
#                if arr[j] < arr[min]:
#                     min = j
#           arr[i],arr[min]=arr[min],arr[i]
#      return arr                


# arr=[3,4,5,1,2]
# print(f(arr))



def f(n):
     count = 0
     for i in range(2,n):
          is_Prime =True
          for j in range(2,int(i**0.5)+1):
               if i % j == 0:
                    is_Prime=False
                    break
          if is_Prime:
               count +=1
     return count


n=10
print(f(n))          