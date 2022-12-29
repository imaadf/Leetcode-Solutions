from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        res = []
        first_word = strs[0]

        for i, letter in enumerate(first_word):
            for word in strs:
                if len(word) == i or word[i] != letter:
                    return ''.join(res)
            res.append(letter)

        return ''.join(res)
