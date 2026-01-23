# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if not root:
            return res 
        q = deque([root])


        while q:
            size = len(q)
            maxVal = float("-inf")

            for _ in range(size):
                node = q.popleft()
                maxVal = max(maxVal,node.val)




                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(maxVal) 
        return res              