# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/

from typing import Optional, Dict


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        valueNewNodeMapper = {}

        def cloneNode(node: Node, valueNewNodeMapper: Dict[int, Node]):
            if node.val in valueNewNodeMapper:
                return valueNewNodeMapper[node.val]

            newNode = Node(node.val)
            valueNewNodeMapper[node.val] = newNode

            for neighbor in node.neighbors:
                newNode.neighbors.append(cloneNode(neighbor, valueNewNodeMapper))

            return newNode

        cloneNode(node, valueNewNodeMapper)

        return valueNewNodeMapper[node.val]

    """
    Initially, I added my new node to the hash after the loop that copies the neighbors because I thought 
    the node needed to be fully constructed with its neighbors first. However, this approach caused an infinite 
    loop, leading to a maximum recursion depth exceeded error. For example, when building node 1, I needed 
    node 2. Then, while building node 2, I needed node 1. The solution is to add the node to the hash before 
    cloning its neighbors, which prevents the recursion issue.
    """
