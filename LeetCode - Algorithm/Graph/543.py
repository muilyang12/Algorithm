# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node):
            nonlocal result

            if not node:
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            result = max(result, leftHeight + rightHeight)

            return max(leftHeight, rightHeight) + 1

        dfs(root)

        return result
