# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isSame(root.left, root.right)

    def isSame(self, node1: TreeNode, node2: TreeNode):
        # Both of them are None.
        if not node1 and not node2:
            return True

        # One of them is None.
        if not node1 or not node2:
            return False

        # None of them is None.
        if node1.val != node2.val:
            return False

        return self.isSame(node1.left, node2.right) and self.isSame(
            node1.right, node2.left
        )
