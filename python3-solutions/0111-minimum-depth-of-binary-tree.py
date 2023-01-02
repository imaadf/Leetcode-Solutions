from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.minimum_depth_helper(root)

    def minimum_depth_helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.minimum_depth_helper(root.left)
        right_height = self.minimum_depth_helper(root.right)

        if not left_height or not right_height:
            return max(left_height, right_height) + 1
        else:
            return min(left_height, right_height) + 1
