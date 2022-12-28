# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs_identical_tree(p, q)

    def dfs_identical_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        identical_left_tree = self.dfs_identical_tree(p.left, q.left)
        identical_right_tree = self.dfs_identical_tree(p.right, q.right)

        return identical_left_tree and identical_right_tree
