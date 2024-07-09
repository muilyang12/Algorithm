# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        self.inorder(root)

        return values[k - 1]

    def inorder(self, node, values):
        if not node:
            return

        self.inorder(node.left)
        values.append(node.val)
        self.inorder(node.right)
