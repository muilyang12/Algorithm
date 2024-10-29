# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
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
