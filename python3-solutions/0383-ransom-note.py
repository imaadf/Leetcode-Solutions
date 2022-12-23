class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        char_to_freq = {}

        for letter in magazine:
            char_to_freq[letter] = char_to_freq.get(letter, 0) + 1

        for letter in ransomNote:
            char_to_freq[letter] = char_to_freq.get(letter, 0) - 1
            if char_to_freq.get(letter) < 0:
                return False

        return True
