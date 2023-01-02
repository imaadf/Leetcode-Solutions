class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        for letter in columnTitle:
            res *= 26
            res += ord(letter) - 64

        return res
