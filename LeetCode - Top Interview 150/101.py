# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/description/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def check_value(left_node, right_node):
            if not left_node and not right_node:
                return True

            if not left_node or not right_node:
                return False

            if left_node.val != right_node.val:
                return False

            return (check_value(left_node.left, right_node.right)) and (
                check_value(left_node.right, right_node.left)
            )

        return check_value(root.left, root.right)

    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = []
        queue.append((root.left, root.right))

        while queue:
            left, right = queue.pop(0)

            if not left and not right:
                continue

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True
