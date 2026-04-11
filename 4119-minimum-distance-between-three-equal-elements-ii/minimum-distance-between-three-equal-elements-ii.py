class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = {}
        for i , val in enumerate(nums):
            positions.setdefault(val, []).append(i)


        ans= float('inf')


        for val , arr in positions.items():
            if len(arr)>=3:
                for i in range(len(arr)-2):
                    span=arr[i+2]-arr[i]
                    ans=min(ans,2*span)
        return ans if ans != float("inf")  else -1              
