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


"""
As you can see, I initially used a "route" parameter in the DFS function. When I ran the code on LeetCode, it ranked only in 
the 5th percentile for runtime, which was disappointing. After reviewing solutions with a similar approach, I realized the 
"route" parameter was unnecessary. All I needed was the maxValue so far. This is a recurring issue for me, especially in 
sliding window problems: I often over-traverse the array when I only need a specific value. Instead, I should focus on tracking 
that value directly.
"""
