# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder_traversal_helper(root, [])

    def inorder_traversal_helper(self, root: Optional[TreeNode], nodes: List[int]) -> List[int]:
        if not root:
            return nodes

        self.inorder_traversal_helper(root.left, nodes)
        nodes.append(root.val)
        self.inorder_traversal_helper(root.right, nodes)

        return nodes
