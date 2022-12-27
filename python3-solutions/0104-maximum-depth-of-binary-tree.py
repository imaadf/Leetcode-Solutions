# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs_depth_helper(root)

    def dfs_depth_helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.dfs_depth_helper(root.left)
        right = self.dfs_depth_helper(root.right)

        return max(left, right) + 1
