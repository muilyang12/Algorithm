# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        self.inorderRecursive(root, result)

        return result

    def inorderRecursive(self, node: Optional[TreeNode], result: List[int]):
        if not node:
            return

        self.inorderRecursive(node.left, result)
        result.append(node.val)
        self.inorderRecursive(node.right, result)
