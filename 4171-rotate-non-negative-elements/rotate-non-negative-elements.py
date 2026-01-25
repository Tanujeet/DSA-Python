class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        
        pos = [x for x in nums if x >= 0]

        n = len(pos)

        if n == 0:
            return nums


        k = k % n

        pos[:] = pos[k:] + pos[:k]


        idx = 0

        for i in range(len(nums)):
            if nums[i]>=0:
                nums[i] = pos[idx] 
                idx +=1

        return nums        

