# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs_subtree_helper(root, subRoot)

    def dfs_subtree_helper(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.dfs_sametree_helper(root, sub_root):
            return True

        left = self.dfs_subtree_helper(root.left, sub_root)
        right = self.dfs_subtree_helper(root.right, sub_root)

        return left or right

    def dfs_sametree_helper(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return root1 == root2
        if root1.val != root2.val:
            return False

        same_left = self.dfs_sametree_helper(root1.left, root2.left)
        same_right = self.dfs_sametree_helper(root1.right, root2.right)

        return same_left and same_right
