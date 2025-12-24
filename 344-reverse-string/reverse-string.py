class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        

        def backtrack(l,r):
            if l >= r:
                return


            s[l],s[r] = s[r],s[l]
            backtrack(l+1,r-1)

        backtrack(0,len(s)-1)        