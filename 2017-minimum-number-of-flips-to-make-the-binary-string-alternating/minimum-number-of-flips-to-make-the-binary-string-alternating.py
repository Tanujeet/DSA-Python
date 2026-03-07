class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s+s

        alt1 = ""
        alt2 = ""



        for i in range(2*n):
            if i % 2:
                alt1 += '1'
                alt2 += '0'
            else:
                alt1+='0'
                alt2+='1'
        

        res =  float('inf')
        diff1 = diff2 = 0
        left = 0


        for right in range(2*n):
            if s[right] != alt1[right]:
                diff1+=1
            if s[right] != alt2[right]:
                diff2 +=1
            

            if right - left + 1 > n:
                if s[left]!= alt1[left]:
                    diff1 -=1
                if s[left] != alt2[left]:
                    diff2 -=1
                left+=1
            


            if right - left + 1 == n:
                res = min(res,diff1,diff2)
        

        return res 


