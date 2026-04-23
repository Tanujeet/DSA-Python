class Solution:
    def getDistances(self, nums: List[int]) -> List[int]:
        seen = defaultdict(list)

        for i,num in enumerate(nums):
            seen[num].append(i)


        res = [0] * len(nums)

        for indices in seen.values():
            n = len(indices)
            prefix = [0] * (n+1)

            for i, idx in enumerate(indices):
                prefix[i+1] = prefix[i] + idx

            

            for i , idx in enumerate(indices):
                left = idx * i - prefix[i]
                right = (prefix[n]- prefix[i+1]) - idx * (n-i-1)
                res[idx] = left + right
        

        return res