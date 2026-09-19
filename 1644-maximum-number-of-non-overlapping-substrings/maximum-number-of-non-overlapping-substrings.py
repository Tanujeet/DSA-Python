class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = {}
        last = {}


        for i , ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            
            last[ch] = i
        


        intervals = []
        for i in range(n):
            if first[s[i]] != i:
                continue 
        

            start , end  = i , last[s[i]]
            j = start
            while j <= end:
                ch = s[j]
                if first[ch] < start:
                    break
                
                end = max(end,last[ch])
                j+=1
            
            else:
                intervals.append((start,end))
        

        intervals.sort(key=lambda x: x[1])
        res = []
        prev_end = -1

        for start,end in intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end
        

        return res 