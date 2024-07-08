# 530. Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)

        result = 100000

        for i in range(len(values) - 1):
            result = min(result, values[i + 1] - values[i])

            if result == 1:
                break

        return result
