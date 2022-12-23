class Solution:
    def longestPalindrome(self, s: str) -> int:

        odd_chars = set()

        for char in s:
            if char not in odd_chars:
                odd_chars.add(char)
            else:
                odd_chars.remove(char)

        if len(odd_chars) == 0:
            return len(s)
        else:
            return len(s) - len(odd_chars) + 1
