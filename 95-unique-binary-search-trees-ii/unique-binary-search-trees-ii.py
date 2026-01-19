# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        #base
        if n == 0:
            return []

        def build(l,r):

            #base case 
            if l > r:
                return [None]

            res = []    


            #recurse for both side 
            for root in range(l,r + 1):
                left = build(l,root-1)   
                right = build(root+1,r)
            

            #combinations
                for lt in left:
                    for rt in right:
                        node = TreeNode(root)
                        node.left = lt
                        node.right = rt
                        res.append(node)


            return res

        return build(1, n)       

