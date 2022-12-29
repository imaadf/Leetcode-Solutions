# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symmetric_helper(root.left, root.right)

    def symmetric_helper(self, left_root: Optional[TreeNode], right_root: Optional[TreeNode]) -> bool:
        if not left_root or not right_root:
            return left_root == right_root

        same_value = left_root.val == right_root.val
        same_inwards = self.symmetric_helper(left_root.right, right_root.left)
        same_outwards = self.symmetric_helper(left_root.left, right_root.right)

        return same_value and same_inwards and same_outwards
