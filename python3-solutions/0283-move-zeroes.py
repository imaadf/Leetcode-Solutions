from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0

        for right, num in enumerate(nums):
            if num != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
