#  Given an array, we have found the number of occurrences of each element in the array.

def frequency(arr,n):
    mp={}
    for n in arr:
        mp[n] = mp.get(n,0)+1
    print(mp)    
        
arr=[10,5,15,10,5]
n=len(arr)
frequency(arr,n)


# Given an array of size N. Find the highest and lowest frequency element.