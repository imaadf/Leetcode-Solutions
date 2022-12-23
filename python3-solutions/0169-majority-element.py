from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count, result = 0, None

        for num in nums:
            if count == 0:
                count, result = 1, num
            elif num == result:
                count += 1
            else:
                count -= 1

        return result
