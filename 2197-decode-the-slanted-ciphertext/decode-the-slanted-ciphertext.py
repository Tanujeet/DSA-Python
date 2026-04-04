class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        res = []

        for i in range(cols):
            idx = i

            while idx < n:
                res.append(encodedText[idx])
                idx += cols + 1
        

        return "".join(res).rstrip()