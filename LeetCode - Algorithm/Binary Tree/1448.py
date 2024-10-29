# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/


from typing import List
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes1(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, route: List[TreeNode], result: List[TreeNode]):
            if not node:
                return

            if all(elem.val <= node.val for elem in route):
                result.append(node)

            route.append(node)

            dfs(node.left, route, result)
            dfs(node.right, route, result)

            route.pop()

        result = []
        dfs(root, [], result)

        return len(result)

    def goodNodes2(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, maxValue: int, result: List[TreeNode]):
            if not node:
                return

            if node.val >= maxValue:
                result.append(node)

                maxValue = node.val

            dfs(node.left, maxValue, result)
            dfs(node.right, maxValue, result)

        result = []
        dfs(root, -math.inf, result)

        return len(result)
