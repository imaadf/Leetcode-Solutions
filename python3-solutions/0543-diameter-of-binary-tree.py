# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        self.dfs_diameter_helper(root)

        return self.max_diameter

    def dfs_diameter_helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.dfs_diameter_helper(root.left)
        right = self.dfs_diameter_helper(root.right)
        self.max_diameter = max(self.max_diameter, left + right)

        return max(left, right) + 1
