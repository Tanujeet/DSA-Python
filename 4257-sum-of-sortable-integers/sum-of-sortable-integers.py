class Solution:
    def divisior(self,nums):
        n = len(nums)
        divisor = []

        for i in range(1,n+1):
            if n % i == 0:
                divisor.append(i)


        return divisor


    def getChunks(self,nums,k):
        n = len(nums)
        chunks= []
        for i in range(0,n,k):
            chunks.append(nums[i:i+k])
        return chunks 

        
    def isValid(self,chunk):
        drops = 0 
        for i in range(len(chunk)-1):

            if chunk[i] > chunk[i+1]:
                drops+=1


        if drops > 1:
            return False

        if drops == 1 and chunk[-1] > chunk[0]:
            return False


        return True 
        
        
    def sortableIntegers(self, nums: list[int]) -> int:
        res = 0
        for k in self.divisior(nums):
            chunks = self.getChunks(nums,k)
            Valid = True

            for i in range(len(chunks)):
                if not self.isValid(chunks[i]):
                    Valid = False
                    break


                if i > 0 and max(chunks[i-1]) > min(chunks[i]):
                    Valid  = False
                    break 
            if Valid:
                res+=k
        return res 
    
        