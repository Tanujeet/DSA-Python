class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0


        for i in range(n):
            CurrSum = 0
            seen = set()

            for j in range(i,n):
                CurrSum += nums[j]

                seen.add(nums[j])

                if CurrSum in seen:
                    count +=1

        return count             