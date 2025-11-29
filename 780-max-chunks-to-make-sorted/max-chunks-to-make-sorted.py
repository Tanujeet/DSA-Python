class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        curr_max = 0

        for i , val in enumerate(arr):
            curr_max = max(curr_max,val)
            if curr_max==i:
                chunks+=1
        return chunks    