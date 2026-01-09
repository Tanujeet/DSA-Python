# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return(0,None)

            leftDepth,leftnode = dfs(node.left)    
            rightDepth,rightnode = dfs(node.right)  
            

            if leftDepth > rightDepth:
                return(leftDepth + 1 , leftnode)

            if rightDepth > leftDepth:
                return (rightDepth + 1 , rightnode) 

            return (leftDepth + 1 , node)

        return dfs(root)[1]        

