# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if not node:
                return None


            left = dfs(node.left)
            right = dfs(node.right)

            selfNode = (node == q)  or (node==p) 


            if (left and right) or (selfNode and left) or (selfNode and right):
                return node



            if left:
                return left

            if right :
                return right

            if selfNode:
                return node

            return None
        return dfs(root)    


       



