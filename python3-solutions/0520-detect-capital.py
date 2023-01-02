class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals = 0

        for letter in word:
            if letter.isupper():
                capitals += 1

        return capitals == 0 or capitals == len(word) or (capitals == 1 and word[0].isupper())
