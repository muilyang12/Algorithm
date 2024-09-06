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
        return self.checkBST(root)

    def checkBST(
        self,
        node: Optional[TreeNode],
        smallerThan: Optional[int] = None,
        largerThan: Optional[int] = None,
    ) -> bool:
        if not node:
            return True

        if node.left and node.left.val >= node.val:
            return False

        if node.left and largerThan and node.left.val <= largerThan:
            return False

        if node.right and node.right.val <= node.val:
            return False

        if node.right and smallerThan and node.right.val >= smallerThan:
            return False

        return self.checkBST(
            node=node.left, smallerThan=node.val, largerThan=largerThan
        ) and self.checkBST(
            node=node.right, smallerThan=smallerThan, largerThan=node.val
        )
