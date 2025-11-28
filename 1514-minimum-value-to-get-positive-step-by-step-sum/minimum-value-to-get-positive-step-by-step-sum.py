class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = 0
        total= 0
        for num in nums:
            total+=num
            min_sum = min(min_sum,total)
        return -min_sum  +1  