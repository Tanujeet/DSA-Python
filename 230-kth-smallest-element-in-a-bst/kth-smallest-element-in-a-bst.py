# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans , count = 0,0

        def bst(node):
            nonlocal ans,count

            if not node:
                return 

            bst(node.left)
            count +=1

            if count == k:
                ans = node.val
                return

            bst(node.right)

        bst(root)
        return ans        