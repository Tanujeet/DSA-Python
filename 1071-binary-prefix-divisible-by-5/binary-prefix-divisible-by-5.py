class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        rev = 0

        for bit in nums:
            rev = (rev * 2 + bit) % 5   
            ans.append(rev == 0)

        return ans
