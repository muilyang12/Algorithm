# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        nodes = []

        def dfs(node):
            if not node:
                return

            nodes.append(node)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        for index, node in enumerate(nodes):
            node.left = None

            if index + 1 < len(nodes):
                node.right = nodes[index + 1]
            else:
                node.right = None
