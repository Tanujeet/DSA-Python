class Solution:
    def minDeletionSize(self, arr: List[str]) -> int:
        res = 0 

        for col in range(len(arr[0])):
            for row in range(1,len(arr)):
                if arr[row][col] < arr[row-1][col]:
                    res+=1
                    break
        return res             
