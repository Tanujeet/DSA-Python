class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        org = x
        digitSum = 0

        while x > 0:
            digitSum += x % 10
            x //= 10



        if org % digitSum == 0:
            return digitSum
        else:
            return -1         
