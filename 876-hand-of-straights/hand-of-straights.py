class Solution:
    def isNStraightHand(self, hand: List[int], k: int) -> bool:
        n = len(hand)

        if n % k !=0:
            return False
        freq = Counter(hand)
        minheap = list(freq.keys())
        heapq.heapify(minheap)

        while minheap:
            start = minheap[0]
            for i in range(start,start + k):
                if freq[i] == 0:
                    return False
                freq[i] -=1 
                if freq[i] == 0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True                 