from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        cache = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset*2 == i:
                offset *= 2

            cache[i] = cache[i - offset] + 1

        return cache
