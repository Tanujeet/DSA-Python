class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            curr = num
            while stack and stack[-1] == curr:
                top = stack.pop()

                curr  = curr + top


            stack.append(curr)


        return stack         
