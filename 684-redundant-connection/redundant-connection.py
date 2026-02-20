class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = list(range(len(edges)+1))

        def find(node):
            if root[node] != node:
                root[node] = find(root[node])
            return root[node]    

        

        for n1,n2 in edges:
            root1,root2= find(n1),find(n2)

            if root1 == root2:
                return [n1,n2]



            root[root2] = root1      