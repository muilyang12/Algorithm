# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/


import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = []
        max_depth = 0

        queue.append((1, root))
        while queue:
            depth, current = queue.pop(0)
            max_depth = max(max_depth, depth)

            if current.left:
                queue.append((depth + 1, current.left))

            if current.right:
                queue.append((depth + 1, current.right))

        return max_depth
