from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        prev_num = None

        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break
            if num == prev_num:
                continue

            left, right = i + 1, len(nums) - 1
            appended = None

            while left < right:
                if nums[left] + nums[right] + num > 0:
                    right -= 1
                elif nums[left] + nums[right] + num < 0:
                    left += 1
                elif appended != nums[left]:
                    res.append([nums[left], nums[right], num])
                    appended = nums[left]
                    left += 1
                else:
                    left += 1

            prev_num = num

        return res
