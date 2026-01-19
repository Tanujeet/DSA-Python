# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        #base Case 
        if not root:
            return []


        #recurse left and right
        leftSum = self.pathSum(root.left,targetSum-root.val)
        rightSum = self.pathSum(root.right,targetSum- root.val)


        res = []
        
        if root.left == None and root.right == None:
            remaining  = targetSum - root.val

            if remaining == 0:
                return [[root.val]]
            else:
                return []    

        for path in leftSum:
            res.append([root.val] + path)

        for path in rightSum:
            res.append([root.val] + path)

        return res     



            

                    
               

        





        