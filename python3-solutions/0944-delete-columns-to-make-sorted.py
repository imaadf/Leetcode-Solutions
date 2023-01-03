from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        res = 0
        string_length, list_length = len(strs[0]), len(strs)

        for l in range(string_length):
            for s in range(list_length):
                if s != 0 and strs[s][l] < strs[s - 1][l]:
                    res += 1
                    break

        return res
