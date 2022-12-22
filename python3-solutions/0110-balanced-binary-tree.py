# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs_balanced_helper(root, 0) != -1

    def dfs_balanced_helper(self, root: Optional[TreeNode], height: int) -> int:
        if not root:
            return height
        if height == -1:
            return -1

        left_height = self.dfs_balanced_helper(root.left, height + 1)
        right_height = self.dfs_balanced_helper(root.right, height + 1)

        if abs(left_height - right_height) > 1:
            return -1
        else:
            return max(left_height, right_height)
