# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.array_to_BST_helper(nums, 0, len(nums) - 1)

    def array_to_BST_helper(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None

        mid = (left + right) // 2

        tree = TreeNode(nums[mid])

        tree.left = self.array_to_BST_helper(nums, left, mid-1)
        tree.right = self.array_to_BST_helper(nums, mid+1, right)

        return tree
