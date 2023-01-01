class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        pattern_to_word = {}

        if len(words) != len(pattern) or len(set(words)) != len(set(pattern)):
            return False

        for i, letter in enumerate(pattern):
            if letter in pattern_to_word and pattern_to_word[letter] != words[i]:
                return False
            pattern_to_word[letter] = words[i]

        return True
