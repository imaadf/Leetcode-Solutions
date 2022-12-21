class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars_to_freq = {}

        for i, _ in enumerate(s):
            chars_to_freq[s[i]] = chars_to_freq.get(s[i], 0) + 1
            chars_to_freq[t[i]] = chars_to_freq.get(t[i], 0) - 1

        return all(value == 0 for value in chars_to_freq.values())
