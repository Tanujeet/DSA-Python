class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        maxWindow = 0
        i = 0

        for j in range(n):
            while nums[j] > nums[i] * k:
                i +=1



            windowSize =j- i + 1
            maxWindow = max(maxWindow,windowSize)


        return n- maxWindow        


   
