class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = [-1] * 26
        saved = [0] * n
        order = []

        stack = [(0, False)]
        while stack:
            node, leaving = stack.pop()
            c = ord(s[node]) - ord('a')
            if leaving:
                last[c] = saved[node]
                continue
            if last[c] != -1:
                new_parent[node] = last[c]
            saved[node] = last[c]
            last[c] = node
            order.append(node)
            stack.append((node, True))
            for ch in children[node]:
                stack.append((ch, False))

        size = [1] * n
        for node in reversed(order):
            if new_parent[node] != -1:
                size[new_parent[node]] += size[node]
        return size