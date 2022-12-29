from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        res = 0

        for i, val in enumerate(nums):
            res ^= i ^ val

        return res ^ len(nums)
