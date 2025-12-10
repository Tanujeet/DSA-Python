class Solution:
    def slidingWindowAtMost(self, nums: List[int], distinctK: int) -> int:
        left = 0
        freq_map = defaultdict(int)
        ans  = 0
        n = len(nums)

        for right in range(n):
            freq_map[nums[right]]+=1


            while len(freq_map) > distinctK:
                freq_map[nums[left]]-=1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left+=1

            ans += right-left+1    
        return ans         

    
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)
      
