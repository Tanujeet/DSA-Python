from sortedcontainers import SortedList

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MX = min(50000, 3 * len(queries)) + 5
        sl = SortedList([0, MX])
        seg = [0] * (4 * MX)
        
        def update(node, start, end, idx, val):
            if start == end:
                seg[node] = val
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(2*node, start, mid, idx, val)
            else:
                update(2*node+1, mid+1, end, idx, val)
            seg[node] = max(seg[2*node], seg[2*node+1])
        
        def query(node, start, end, l, r):
            if r < start or end < l:
                return 0
            if l <= start and end <= r:
                return seg[node]
            mid = (start + end) // 2
            return max(
                query(2*node, start, mid, l, r),
                query(2*node+1, mid+1, end, l, r)
            )
        
        update(1, 0, MX-1, MX, MX)
        ans = []
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = sl.bisect_right(x)
                prev = sl[idx - 1]
                nxt = sl[idx]
                sl.add(x)
                update(1, 0, MX-1, x, x - prev)
                update(1, 0, MX-1, nxt, nxt - x)
            else:
                x, sz = q[1], q[2]
                idx = sl.bisect_right(x)
                prev = sl[idx - 1]
                max_gap = max(
                    query(1, 0, MX-1, 0, x),
                    x - prev
                )
                ans.append(max_gap >= sz)
        
        return ans