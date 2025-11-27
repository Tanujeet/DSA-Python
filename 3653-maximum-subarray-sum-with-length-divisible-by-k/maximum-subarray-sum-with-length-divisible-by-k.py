class Solution:
    def maxSubarraySum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        pre = 0

        bucket = {i: float('inf') for i in range(k)}
        bucket[0] = 0  

        best = -10**18

        for i,num in enumerate(arr,1):
            pre+=num
            g = i % k

            best = max(best,pre-bucket[g])
            bucket[g] = min(bucket[g], pre)


        return best    