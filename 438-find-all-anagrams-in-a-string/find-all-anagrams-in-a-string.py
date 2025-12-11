class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m=len(p)
        left = 0
        ans = []
        window = Counter()
        target = Counter(p)

     
        for right in range(n):
           window[s[right]]+=1
      
           if right - left + 1 > m:
            window[s[left]]-=1
            if window[s[left]]==0:
                del window[s[left]]
            left+=1


           if right - left + 1 == m:
            if window == target:
                ans.append(left)    
            
        
                

   
        return ans