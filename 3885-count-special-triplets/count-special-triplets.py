class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        right = Counter(nums)
        left = Counter()

        ans = 0

        for j ,num in enumerate(nums):
            right[num]-=1
            target = 2 * num

            L = left[target]
            R = right[target]

            ans = (ans+L*R) % MOD

            left[num]+=1


        return ans    