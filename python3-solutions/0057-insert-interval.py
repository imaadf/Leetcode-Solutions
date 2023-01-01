from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        intervals_added = 0

        for i, current_interval in enumerate(intervals):
            if current_interval[0] > newInterval[1]:
                break
            elif current_interval[1] < newInterval[0]:
                res.append(current_interval)
            else:
                newInterval[0] = min(current_interval[0], newInterval[0])
                newInterval[1] = max(current_interval[1], newInterval[1])

            intervals_added += 1

        res.append(newInterval)

        for i in range(intervals_added, len(intervals)):
            res.append(intervals[i])

        return res
