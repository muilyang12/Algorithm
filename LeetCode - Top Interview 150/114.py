# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # time complexity: O(2n) = O(n)
    def flatten1(self, root: Optional[TreeNode]) -> None:
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

    # time complexity: O(n)
    def flatten2(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            if len(stack) > 0:
                node.right = stack[-1]

            node.left = None

    # time complexity: O(n)
    # 방식은 멋진데 생각하기가 진짜 힘들 것 같은데...
    def flatten3(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if not node:
                return

            tail_from_left = dfs(node.left)
            tail_from_right = dfs(node.right)

            if tail_from_left:
                tail_from_left.right = node.right
                node.right = node.left
                node.left = None

            return tail_from_right or tail_from_left or node

        dfs(root)
