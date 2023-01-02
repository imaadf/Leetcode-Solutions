# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.pathsum_helper(root, targetSum, 0)

    def pathsum_helper(self, root: Optional[TreeNode], target_sum: int, curr_sum: int) -> bool:
        if not root:
            return False

        curr_sum += root.val

        if curr_sum == target_sum and not root.left and not root.right:
            return True

        left = self.pathsum_helper(root.left, target_sum, curr_sum)
        right = self.pathsum_helper(root.right, target_sum, curr_sum)

        return left or right
