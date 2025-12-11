class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        base = 0
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]

        gain = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                gain += customers[i]

        max_gain = gain

        left = 0
        for right in range(minutes, n):

           
            if grumpy[right] == 1:
                gain += customers[right]

         
            if grumpy[left] == 1:
                gain -= customers[left]

            left += 1
            max_gain = max(max_gain, gain)

        return base + max_gain
