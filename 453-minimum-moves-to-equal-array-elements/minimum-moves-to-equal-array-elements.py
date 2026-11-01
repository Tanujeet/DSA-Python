class Solution:
    def minMoves(self, nums: List[int]) -> int:
   
        smallest = min(nums)

    
        moves = sum(x - smallest for x in nums)


        return moves