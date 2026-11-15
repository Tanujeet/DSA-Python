class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7


        even_count = 1
        odd_count = 0

        running_sum = 0
        answer = 0


        for num in arr:
     
            running_sum = (running_sum + num) % 2

          
            if running_sum == 1:
                answer += even_count
                odd_count += 1
      
            else:
                answer += odd_count
                even_count += 1

   
        return answer % MOD