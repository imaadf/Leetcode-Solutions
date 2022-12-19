from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment_to_index = {}

        for index, num in enumerate(nums):
            compliment = target - num
            if(compliment in compliment_to_index):
                return [index, compliment_to_index[compliment]]
            compliment_to_index[num] = index

        return None
