# selection sort

c =[-3,3,2,1,-5,-3,7,2,2]
def f(arr):
    n =len(arr)
    for i in range(n):
        min =i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
print(f(c))                