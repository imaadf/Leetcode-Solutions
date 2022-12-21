from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                max_profit = max(max_profit, prices[right] - prices[left])

            right += 1

        return max_profit
