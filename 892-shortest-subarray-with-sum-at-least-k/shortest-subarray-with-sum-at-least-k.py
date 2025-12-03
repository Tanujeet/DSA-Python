class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        prefix = 0
        n = len(nums)
        dq = deque()
        dq.append((0,0))


        for i , num in enumerate(nums,1):
            prefix+=num

            while dq  and prefix - dq[0][0] >=k:
                ans = min(ans , i - dq[0][1])
                dq.popleft()


            while dq and prefix <=dq[-1][0]:
                dq.pop()    
            dq.append((prefix,i))    



        return ans if ans != float('inf') else -1    