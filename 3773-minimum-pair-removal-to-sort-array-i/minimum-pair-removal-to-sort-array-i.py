class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0

        def isSorted(nums):
            n = len(nums)

            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    return False

            return True


        while not isSorted(nums):
            n = len(nums)
            minSum = float("inf")
            idx = 0

            for i in range(n-1):
                summation = nums[i] + nums[i+1]
                if summation < minSum:
                    minSum = summation
                    idx = i


            nums[idx] = nums[idx] + nums[idx+1]
            nums.pop(idx+1)
            count +=1

        return count    
