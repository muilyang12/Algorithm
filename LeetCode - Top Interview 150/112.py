# 112. Path Sum
# https://leetcode.com/problems/path-sum/description/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = []
        stack.append((root, 0))

        while stack:
            node, prev_sum = stack.pop()
            current_sum = prev_sum + node.val

            if node.right:
                stack.append((node.right, current_sum))
            if node.left:
                stack.append((node.left, current_sum))

            if not node.right and not node.left and current_sum == targetSum:
                return True

        return False

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True

        next_target_sum = targetSum - root.val

        return self.hasPathSum2(root.right, next_target_sum) or self.hasPathSum2(
            root.left, next_target_sum
        )
