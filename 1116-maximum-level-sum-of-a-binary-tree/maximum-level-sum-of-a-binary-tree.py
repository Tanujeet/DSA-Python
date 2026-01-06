# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q= deque([root])
        maxSum = float('-inf')

        level,res = 0,1

        while q:
            total = 0
            level+=1

            for _ in range(len(q)):
                node = q.popleft()
                total+= node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if total > maxSum:
                maxSum  = total
                res = level

        return res                 

