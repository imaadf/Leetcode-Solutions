# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.old_to_new = {}

        if not node:
            return None

        return self.clone_graph_helper(node)

    def clone_graph_helper(self, curr_node: 'Node') -> 'Node':
        if curr_node in self.old_to_new:
            return self.old_to_new[curr_node]

        copy_node = Node(curr_node.val)

        self.old_to_new[curr_node] = copy_node

        for neighbor in curr_node.neighbors:
            result_node = self.clone_graph_helper(neighbor)
            copy_node.neighbors.append(result_node)

        return copy_node
