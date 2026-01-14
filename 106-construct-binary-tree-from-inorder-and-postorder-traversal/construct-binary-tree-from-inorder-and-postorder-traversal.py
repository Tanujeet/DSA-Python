# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index ={}

        for i in range(len(inorder)):
            index[inorder[i]] = i


        def build(inStart,inEnd,postStart,postEnd):
            if inStart > inEnd or postStart > postEnd:
                return None

            rootval = postorder[postEnd]
            root = TreeNode(rootval)

            idx = index[rootval]
            leftSize = idx - inStart 

            root.right = build(idx+1,inEnd,postStart + leftSize,postEnd - 1)
            root.left = build(inStart,idx-1,postStart,postStart + leftSize - 1)

            return root

        return build(0,len(inorder)-1,0,len(postorder)-1)        