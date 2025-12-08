class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        maxq = deque()
        ans = 0
        left = 0
        run_sum = 0

        for right in range(len(chargeTimes)):
            while maxq and chargeTimes[maxq[-1]] <= chargeTimes[right]:
                maxq.pop()
            maxq.append(right)

            run_sum += runningCosts[right]
            

            while maxq and (chargeTimes[maxq[0]] + (right - left + 1 ) * run_sum ) > budget:
                if maxq[0] ==left :
                    maxq.popleft()

                run_sum -= runningCosts[left]
                left+=1

            ans = max(ans,right-left+1)        


        return ans
