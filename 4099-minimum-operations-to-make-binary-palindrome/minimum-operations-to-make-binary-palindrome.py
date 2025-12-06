class Solution:
    def is_pal(self,x):
        s = bin(x)[2:]
        return s == s[::-1]

        
    def minFlips(self,nums:List[int])->List[int]:
        if self.is_pal(nums):
            return 0 


        left = nums-1    
        right = nums+1
        steps=1

        while True:
            if left >=0 and self.is_pal(left):
                return steps
            if self.is_pal(right):
                return steps

            left-=1
            right+=1
            steps+=1
            
        
    def minOperations(self, nums: List[int]) -> List[int]:
        return [self.minFlips(x) for x in nums]
        