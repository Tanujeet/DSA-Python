def f(arr):
     for i in range(len(arr)):
          min = i
          for j in range(1,len(arr)):
               if arr[j]<arr[i]:
                    min = j
               arr[i],arr[min]=arr[arr],arr[i]


    return arr                