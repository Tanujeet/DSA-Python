class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        sm = [0] * (4 * n)   # segment sums of f
        lz = [0] * (4 * n)   # pending adds

        def push(o, l, r):
            if lz[o]:
                m = (l + r) // 2
                for c, a, b in ((2*o, l, m), (2*o+1, m+1, r)):
                    sm[c] += lz[o] * (b - a + 1)
                    lz[c] += lz[o]
                lz[o] = 0

        # returns sum of f on [L, R], then adds 1 to every f on [L, R]
        def query_add(o, l, r, L, R):
            if L <= l and r <= R:
                res = sm[o]
                sm[o] += r - l + 1
                lz[o] += 1
                return res
            push(o, l, r)
            m = (l + r) // 2
            res = 0
            if L <= m:
                res += query_add(2*o, l, m, L, R)
            if R > m:
                res += query_add(2*o+1, m+1, r, L, R)
            sm[o] = sm[2*o] + sm[2*o+1]
            return res

        last = {}
        cur = ans = 0
        for r, x in enumerate(nums):
            p = last.get(x, -1)
            s = query_add(1, 0, n - 1, p + 1, r)
            cur = (cur + 2 * s + (r - p)) % MOD
            ans = (ans + cur) % MOD
            last[x] = r
        return ans