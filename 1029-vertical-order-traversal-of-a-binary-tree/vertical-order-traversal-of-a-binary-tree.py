# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        map= {}
        def dfs(node,row,col):
            if  node == None:
                return 

            if col not in map:
                map[col] = []
           
            map[col].append([row,node.val])
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)    

        dfs(root,0,0)

        ans = []

        for col in sorted(map.keys()):       
            map[col].sort()                  
            colValues = []

            for row, val in map[col]:
                colValues.append(val)

            ans.append(colValues)

        return ans    

