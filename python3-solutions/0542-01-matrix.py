from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        columns = len(mat[0])

        self.res = [[-1] * columns for _ in range(rows)]
        to_search = deque()

        for i, row in enumerate(mat):
            for j, value in enumerate(row):
                if value == 0:
                    self.res[i][j] = 0
                    to_search.append([i, j])

        while to_search:
            search_element = to_search.popleft()

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for vertical, horizontal in directions:

                search_row = search_element[0] + vertical
                search_column = search_element[1] + horizontal

                if search_row < 0 or search_column < 0 or search_row >= rows or search_column >= columns:
                    continue
                if self.res[search_row][search_column] != -1:
                    continue

                self.res[search_row][search_column] = self.res[search_element[0]
                                                               ][search_element[1]] + 1

                to_search.append([search_row, search_column])

        return self.res
