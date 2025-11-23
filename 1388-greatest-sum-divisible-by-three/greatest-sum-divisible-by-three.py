class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sum_all = sum(nums)

        if sum_all % 3 == 0:
            return sum_all

        mod1 = sorted([x for x in nums if x % 3 == 1])
        mod2 = sorted([x for x in nums if x % 3 == 2])

        if sum_all % 3 == 1:
            option1 = mod1[0] if mod1 else +inf
            option2 = mod2[0] + mod2[1] if len(mod2) >= 2 else +inf
            return sum_all - min(option1, option2)

        if sum_all % 3 == 2:
            option1 = mod2[0] if mod2 else +inf
            option2 = mod1[0] + mod1[1] if len(mod1) >= 2 else +inf
            return sum_all - min(option1, option2)
