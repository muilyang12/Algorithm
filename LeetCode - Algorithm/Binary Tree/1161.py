# 1161. Maximum Level Sum of a Binary Tree
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

from typing import Optional
from collections import deque
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)

        sums = []

        while queue:
            currentSum = 0
            tempNodes = []

            while queue:
                node = queue.popleft()

                currentSum += node.val

                if node.left:
                    tempNodes.append(node.left)
                if node.right:
                    tempNodes.append(node.right)

            sums.append(currentSum)

            for node in tempNodes:
                queue.append(node)

        result = -1
        max = -math.inf
        for index, sum in enumerate(sums):
            if sum > max:
                max = sum
                result = index

        return result + 1
