# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []

        def inorder(node):
            if not node:
                return True

            left_result = inorder(node.left)
            if not left_result:
                return False

            if len(values) > 0 and values[-1] >= node.val:
                return False

            values.append(node.val)

            right_result = inorder(node.right)
            if not right_result:
                return False

            return True

        result = inorder(root)

        return result
