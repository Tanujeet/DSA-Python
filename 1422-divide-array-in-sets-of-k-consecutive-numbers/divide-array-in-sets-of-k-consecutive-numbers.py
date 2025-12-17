class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        freq = Counter(nums)
        minheap = list(freq.keys())
        heapq.heapify(minheap)

        while minheap:
            start = minheap[0]
            for i in range(start,start + k):
                if freq[i] == 0:
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    if i != minheap[0]: 
                        return False
                    heapq.heappop(minheap)
        return True                   
