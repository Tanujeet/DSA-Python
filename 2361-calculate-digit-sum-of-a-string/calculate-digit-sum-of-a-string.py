class Solution:
    def digitSum(self, s: str, k: int) -> str:
   
        while len(s) > k:
            parts = []

           
            for i in range(0, len(s), k):
                group = s[i:i + k]       

            
                total = sum(int(ch) for ch in group)

                parts.append(str(total))

            s = "".join(parts)

       
        return s