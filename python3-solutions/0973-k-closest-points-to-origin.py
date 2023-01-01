import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []
        heapq.heapify(res)

        for i, point in enumerate(points):
            x = point[0]
            y = point[1]

            heapq.heappush(res, [-(x**2 + y**2), x, y])
            if len(res) > k:
                heapq.heappop(res)

        return ([x, y] for _, x, y in res)
