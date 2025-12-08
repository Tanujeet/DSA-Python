class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        minq = deque()
        maxq = deque()
        cnt = 0
        left  = 0

        for right , num in enumerate(nums):
            while maxq and nums[maxq[-1]] < num:
                maxq.pop()
            maxq.append(right)    

            while minq and nums[minq[-1]] > num:
                minq.pop()
            minq.append(right)    


            while maxq and minq and nums[maxq[0]] - nums[minq[0]] >2:
                if maxq[0] <minq[0]:
                    left = maxq[0]+1
                    maxq.popleft()
                else:
                    left = minq[0]+1
                    minq.popleft()
            cnt += right - left +1        






        return cnt
