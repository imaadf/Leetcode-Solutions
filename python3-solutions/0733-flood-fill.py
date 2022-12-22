from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or image[sr][sc] == color:
            return image

        self.dfs_fill_helper(image, sr, sc, color, image[sr][sc])
        return image

    def dfs_fill_helper(self, image: List[List[int]], row: int, column: int, color: int, initialColor: int) -> List[List[int]]:
        if row >= len(image) or column >= len(image[0]) or row < 0 or column < 0 or image[row][column] != initialColor:
            return image

        image[row][column] = color

        image = self.dfs_fill_helper(image, row+1, column, color, initialColor)
        image = self.dfs_fill_helper(image, row-1, column, color, initialColor)
        image = self.dfs_fill_helper(image, row, column+1, color, initialColor)
        image = self.dfs_fill_helper(image, row, column-1, color, initialColor)

        return image
