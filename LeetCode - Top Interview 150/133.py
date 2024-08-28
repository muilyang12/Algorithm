# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/


from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        val_to_new = {}

        def clone(node):
            if node.val in val_to_new:
                return val_to_new[node.val]

            new_node = Node(node.val)
            val_to_new[node.val] = new_node

            for neigh in node.neighbors:
                new_node.neighbors.append(clone(neigh))

            return new_node

        return clone(node)
