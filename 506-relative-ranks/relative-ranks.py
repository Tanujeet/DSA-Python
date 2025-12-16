class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        n = len(scores)
        result = [0] * n

        heap = []

        for i , score in enumerate(scores):
            heapq.heappush(heap,(-score,i))

        rank = 1
        while heap:
            _,index = heapq.heappop(heap)
            if rank == 1:
                result[index] = "Gold Medal"
            elif rank == 2:
                result[index] = "Silver Medal"
            elif rank == 3:
                result[index] = "Bronze Medal"
            else:
                result[index] =  str(rank)
            rank+=1
        return result                    
