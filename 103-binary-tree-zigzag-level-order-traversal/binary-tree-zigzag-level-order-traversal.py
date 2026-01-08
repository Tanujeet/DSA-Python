# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        def bfs(root):

            if not root:
                return []

            q = deque([root])
            res = []
            levelIndex = 0

            while q:
                level = []
                size = len(q)

                for _ in range(size):
                    node = q.popleft()
                    level.append(node.val)


                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

                if levelIndex %2 == 1:
                    level.reverse()        

                res.append(level)
                levelIndex +=1

            return res    
        return bfs(root)


