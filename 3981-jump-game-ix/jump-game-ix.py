class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        res = [0] * n


        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = max(prefix[i-1],nums[i])
        

        suffix[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            suffix[i] = min(suffix[i+1],nums[i])
        


        res[-1] = prefix[-1]

        for i in range(n-2,-1,-1):
            if prefix[i] > suffix[i+1]:
                res[i] = res[i+1]
            

            else:
                res[i] = prefix[i]
        

        return res 