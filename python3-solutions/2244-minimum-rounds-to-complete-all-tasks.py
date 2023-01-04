from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        res = 0
        frequencies = Counter(tasks)

        for freq in frequencies.values():
            if freq == 1:
                return -1
            elif freq % 3 == 0:
                res += freq // 3
            elif (freq - 2) % 3 == 0:
                res += ((freq - 2) // 3) + 1
            elif (freq - 4) % 3 == 0:
                res += ((freq - 4) // 3) + 2
            else:
                res += freq // 2

        return res
