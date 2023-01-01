from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        nodes = deque()
        nodes.append([root, 1])

        while nodes:
            popped = nodes.popleft()
            node = popped[0]
            level = popped[1]

            if not node:
                continue

            if len(res) != level:
                res.append([node.val])
            else:
                res[level - 1].append(node.val)

            left_child = node.left
            right_child = node.right

            if left_child:
                nodes.append([left_child, level + 1])
            if right_child:
                nodes.append([right_child, level + 1])

        return res
