from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) - sum(cost) < 0:
            return -1

        total, index = 0, 0

        for i, _ in enumerate(gas):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                index = i + 1

        return index
