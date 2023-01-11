from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort()

        prev_start, prev_end = points[0][0], points[0][1]
        res = 1

        for start, end in points:
            if start > prev_end:
                prev_start, prev_end = start, end
                res += 1
            else:
                prev_end = min(prev_end, end)

        return res
