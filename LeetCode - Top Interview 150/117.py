# 117. Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/


from typing import List, Optional


class Node:
    def __init__(
        self,
        val=0,
        left=None,
        right=None,
        next=None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return root

        queue = []
        queue.append((root, 1))

        prev_depth = 0
        dummy_node = Node(-1)
        prev_node = dummy_node

        while queue:
            node, depth = queue.pop(0)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

            if prev_depth != depth:
                prev_depth = depth

                prev_node.next = None
                prev_node = node
            else:
                prev_node.next = node
                prev_node = node

        return root
