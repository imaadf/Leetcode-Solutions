from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs.sort()
        res = 0

        for cost in costs:
            if cost > coins:
                break
            coins -= cost
            res += 1

        return res
