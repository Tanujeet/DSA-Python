# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []


        freq = defaultdict(int)    
        

        def dfs(node):
    
            if not node:
                return 0 



            leftSum = dfs(node.left)
            rightSum = dfs(node.right)

            subtreesum = node.val + leftSum + rightSum

            freq[subtreesum]+=1


            return subtreesum
        dfs(root)


        maxfreq = max(freq.values())


        res = []

        for s in freq:
            if freq[s] == maxfreq:
                res.append(s)
        return res            
 

