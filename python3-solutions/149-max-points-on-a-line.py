from collections import defaultdict
from typing import List, Tuple


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 2:
            return len(points)

        res = 0

        for i, _ in enumerate(points):

            counts = defaultdict(lambda: 1)

            for j in range(i + 1, len(points)):
                counts[self.get_line_equation(points[i], points[j])] += 1

            if counts:
                res = max(res, max(counts.values()))

        return res

    def get_line_equation(self, point_a: List[int], point_b: List[int]) -> Tuple[int]:

        if point_a[0] == point_b[0]:
            return (point_a[0])

        slope = (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])
        y_intercept = point_a[1] - (slope * point_a[0])

        return (slope, y_intercept)
