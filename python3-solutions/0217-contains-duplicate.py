from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        unique_values = set()

        for num in nums:
            if num in unique_values:
                return True
            unique_values.add(num)

        return False
