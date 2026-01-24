class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort()
        i = 0
        j = n - 1
        maxPairSum = 0

        while i <=j:
            #hr baar do pair bnau and unka sum kro
            pairs = nums[i] + nums[j] 

            #fir sare pair ke sum ka max nikalo aur retrurn kro
            maxPairSum = max(maxPairSum,pairs)

            i+=1
            j-=1 




        return maxPairSum    

