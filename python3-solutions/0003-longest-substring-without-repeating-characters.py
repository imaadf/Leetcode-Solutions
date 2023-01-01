class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_length = 1
        left = 0
        chars_used = set()

        for right, letter in enumerate(s):
            while letter in chars_used:
                chars_used.remove(s[left])
                left += 1
            chars_used.add(letter)
            max_length = max(max_length, right-left+1)

        return max_length
