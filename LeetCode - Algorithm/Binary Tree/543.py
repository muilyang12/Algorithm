# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getDepthAndUpdateResult(root)

        return self.result

    def getDepthAndUpdateResult(self, node: TreeNode, currentDepth: int = 1) -> int:
        if not node:
            return currentDepth - 1

        leftDepth = self.getDepthAndUpdateResult(node.left, currentDepth + 1)
        rightDepth = self.getDepthAndUpdateResult(node.right, currentDepth + 1)

        self.result = max(
            self.result, leftDepth - currentDepth + rightDepth - currentDepth
        )

        return max(leftDepth, rightDepth)
