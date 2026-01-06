class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)

        for k , v in freq.items():
            if v >= 2:
                return True

        return False    