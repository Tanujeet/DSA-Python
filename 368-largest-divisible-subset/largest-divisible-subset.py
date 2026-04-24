class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n
        prev = [-1] * n


        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i]= dp[j] + 1
                    prev[i] = j
        

        max_idx = max(range(n), key= lambda x:dp[x])


        res = []
        i = max_idx

        while i != -1:
            res.append(nums[i])
            i = prev[i]
        

        return res[::-1]