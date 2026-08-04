class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not  nums:
            return num
        full = set(range(min(nums),max(nums)+1))
        missing = sorted(list(full - set(nums)))
        return missing
       