class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        nines = sum // 9
        rest = sum % 9
        result = "9" * nines
        if rest > 0:
            result += str(rest)
        result += "0" * (num - len(result))
        return result